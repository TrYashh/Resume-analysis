function validateFileSize(input) {
    const file = input.files[0];
    if (file && file.size > 10 * 1024 * 1024) { // 10 MB in bytes
        alert("File size exceeds 10 MB. Please upload a smaller file.");
        input.value = ""; // Clear the input
    }
}

function updateFileName(input) {
    const fileNameSpan = document.getElementById("file-name");
    if (input.files.length > 0) {
        fileNameSpan.textContent = input.files[0].name;
    } else {
        fileNameSpan.textContent = "No file chosen";
    }
}

// ...existing code...