//  global variables added to top of js file, js hint kept showing these as unused because they are in an external file
/* global swal */
/* global emailjs */

// function to send email in contact form.
(function () {
  emailjs.init("ga5PLTovBmNLpTpJO");
})();

// Subscribe email function, if a user inputs their email address into the subscribe-box they will get added to our contact list
function validate() {
  let subscribeEmail = document.getElementById("subscribe_email");
  let subscribeSubmit = document.getElementById("subscribe-submit");
  subscribeSubmit.addEventListener("click", (e) => {
    e.preventDefault();
    if (subscribeEmail.value == "") {
      subEmptyerror();
    } else if (
      !/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(
        subscribeEmail.value
      )
    ) {
      subInvalid();
    } else {
      sendmail(subscribeEmail.value);
      subSuccess();
    }
  });
}
validate();

// function used to send the email using emailjs
/**
 *
 * @param email [subscribe email]
 */
function sendmail(email) {
  emailjs.send("service_qknmyza", "taco-y-tequila", {
    'subscribe_email': email,
  });
}

/**
 * Sweet Alert library used to display feedback on form submission
 * Function called if fields are empty and a submit is attempted
 */
function subEmptyerror() {
  swal({
    icon: "error",
    title: "Oops...",
    text: "Fields cannot be empty!",
  });
}

//   function called if the submit button is successful
function subSuccess() {
  swal({
    icon: "success",
    title: "Success...",
    text: "You have subscribed!",
  });
}

//   function called if an invalid email address is used
function subInvalid() {
  swal({
    icon: "error",
    title: "Oops...",
    text: "Invalid Email Address",
  });
}
