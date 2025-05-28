document.addEventListener("DOMContentLoaded", function () {
    let dropbtn = document.querySelector(".dropbtn");
    let dropdownContent = document.querySelector(".dropdown-content");

    if (dropbtn && dropdownContent) {
        dropbtn.addEventListener("click", function (event) {
            event.stopPropagation();
            dropdownContent.style.display = dropdownContent.style.display === "block" ? "none" : "block";
        });

        // Close dropdown when clicking outside
        document.addEventListener("click", function () {
            dropdownContent.style.display = "none";
        });
    }
});
