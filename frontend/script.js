function startRecording() {
    alert("הקלטה הופעלה!");
}

function stopRecording() {
    alert("הקלטה נעצרה!");
}

function search() {
    let query = document.getElementById("search-box").value;
    alert("מחפש: " + query);
}

// פותח פופ-אפ למחשב
function openPopup(computerName) {
    document.getElementById("popup-title").innerText = "אפשרויות עבור " + computerName;
    document.getElementById("popup").style.display = "block";
}

// סוגר את הפופ-אפ
function closePopup() {
    document.getElementById("popup").style.display = "none";
}

// חיפוש בפופ-אפ
function searchPopup() {
    let query = document.getElementById("popup-search").value;
    alert("מחפש בתוך המחשב: " + query);
}
