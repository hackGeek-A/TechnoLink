//collecting data from the user
//#1 getting the field from the user

//getting the submit button
let submitBtn = document.getElementById("submit");
submitBtn.addEventListener("click", function () {
    let field = document.getElementById("field_choice").value;
    let specialty = document.getElementById("specialty_choice").value;
    let fullName = document.getElementById("full_name").value;
    let courseLength = document.getElementById("course_length").value;
    const fileContent = fullName + "\n" + field + "\n" + specialty + "\n" + courseLength;
    const fileName = `${fullName}.txt`;
    //create a new Blob with the file content
    const blob = new Blob([fileContent], { type: 'text/plain' });
    //create a new file objcet with the blob
    const file = new File([blob], fileName);
    alert(fileContent);
});
