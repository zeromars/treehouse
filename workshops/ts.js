//optionally typed
var name = "Andrew";
var name = "Andrew";
function sendEmail(contact) {
    console.log(contact.name + " <" + contact.email + ">");
}
sendEmail({ name: "Andrew Chalkley", email: "ansrew@teamtreehouse.com" });
var Company = (function () {
    function Company(companyName, emailAddress) {
        this.name = companyName;
        this.email = emailAddress;
    }
    return Company;
})();
var treehouse = new Company("Treehouse", "support@teamtreegouse.com");
sendEmail(treehouse);
