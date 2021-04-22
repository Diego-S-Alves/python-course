function createPDF() {
var copyFile = DriveApp.getFileById('ID of template Doc').makeCopy();
 copyId = copyFile.getId();
 copyDoc = DocumentApp.openById(copyId);
var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Name of Sheet");
var lastRow = sheet.getLastRow();
var variableOne = sheet.getRange(lastRow, Column Number).getValue()
var position = sheet.getRange(lastRow, 2).getValue()
var department = sheet.getRange(lastRow, 3).getValue();

var replace_values = [variableOne, position, department];
for (var i = 0; i < replace_values.length; i++) {
copyDoc.replaceText('##Variable as it’s written in the template - must match exactly##', variableOne);
copyDoc.replaceText('##Employee position name##', position);
copyDoc.replaceText('##Department##', department);
}
copyDoc.saveAndClose()

//PDF file name - In this example, the PDF includes the value from Column 3 in addition to the file name
var PDF_FILE_NAME = sheet.getRange(lastRow, 3).getValue() + "_File name";
var newFile = DriveApp.createFile(copyFile.getAs('application/pdf'))
 if (PDF_FILE_NAME !== '') {
   newFile.setName(PDF_FILE_NAME)
 }
//Defines who to send the email to. In this example, Column 2 is the respondent's email address
var  userEmails = sheet.getRange(lastRow, 2).getValue() + ", winning.workplace.tools@whirlpool.com - optional email address to copy on responses"

//Configures the email notification with completed template attached. (recipients, subject, email body, and email subject)
var blob = Utilities.newBlob('');
MailApp.sendEmail(userEmails,"Email Subject Line_" + department (optional variable) + "_(optional - adding a space)" + variableOne (optional variable), "This is the email text." + newFile, {name:"Name of the team sending the email (ex “Google Team”)", attachments: [newFile.getAs(MimeType.PDF), blob]});
copyFile.setTrashed(true);
newFile.setTrashed(true);
}



