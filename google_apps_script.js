function doGet(e) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var result = {};

  // List of sheets to Read
  var sheets = ["Rooms", "Users", "Tasks", "Guests", "Attendance", "Settings"];

  sheets.forEach(function (name) {
    var sheet = ss.getSheetByName(name);
    if (!sheet) {
      result[name] = []; // Empty if doesn't exist
    } else {
      // GetDataRange includes header, we assume data starts/includes appropriate format
      var data = sheet.getDataRange().getValues();
      result[name] = data;
    }
  });

  return ContentService.createTextOutput(JSON.stringify(result)).setMimeType(
    ContentService.MimeType.JSON
  );
}

function doPost(e) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var data = JSON.parse(e.postData.contents); // Expecting { "Rooms": [[...]], "Users": [[...]] }

  var sheets = ["Rooms", "Users", "Tasks", "Guests", "Attendance", "Settings"];

  sheets.forEach(function (name) {
    if (data[name]) {
      var sheet = ss.getSheetByName(name);
      if (!sheet) {
        sheet = ss.insertSheet(name);
      }

      sheet.clear(); // Overwrite mode matching file system behavior

      if (data[name].length > 0) {
        // GAS requires a 2D array. Ensure strings/numbers are clean.
        var rows = data[name];
        sheet.getRange(1, 1, rows.length, rows[0].length).setValues(rows);
      }
    }
  });

  return ContentService.createTextOutput(
    JSON.stringify({ status: "success" })
  ).setMimeType(ContentService.MimeType.JSON);
}
