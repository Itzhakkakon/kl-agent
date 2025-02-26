let isRecording = false;

function startRecording() {
    const button = event.target;
    if (!isRecording) {
        isRecording = true;
        button.style.backgroundColor = '#f44336';
        button.innerHTML = 'מקליט... <div class="loading"></div>';
        showNotification("הקלטה הופעלה!");
    }
}

function stopRecording() {
    const recordButton = document.querySelector('button');
    if (isRecording) {
        isRecording = false;
        recordButton.style.backgroundColor = '';
        recordButton.textContent = 'הפעל הקלטה';
        showNotification("הקלטה נעצרה!");
    }
}

function search() {
    const searchBox = document.getElementById('search-box');
    const searchTerm = searchBox.value;
    searchBox.insertAdjacentHTML('afterend', '<div class="loading"></div>');
    setTimeout(() => {
        const loadingEl = document.querySelector('.loading');
        if (loadingEl) loadingEl.remove();
        showNotification("מחפש: " + searchTerm);
    }, 1000);
}

// פותח פופ-אפ למחשב
function openPopup(computerName) {
    const popup = document.getElementById('popup');
    const popupContent = popup.querySelector('.popup-content');
    const popupTitle = document.getElementById('popup-title');
    popup.style.display = 'block';
    popup.classList.add('active');
    popupTitle.textContent = computerName;
    document.body.style.overflow = 'hidden';
    requestAnimationFrame(() => {
        popupContent.style.transform = 'translateY(0)';
        popupContent.style.opacity = '1';
    });
}

// סוגר את הפופ-אפ
function closePopup() {
    const popup = document.getElementById('popup');
    const popupContent = popup.querySelector('.popup-content');
    popupContent.style.transform = 'translateY(20px)';
    popupContent.style.opacity = '0';
    popup.classList.remove('active');
    setTimeout(() => {
        popup.style.display = 'none';
        document.body.style.overflow = 'auto';
    },300);
}

// חיפוש בפופ-אפ
function searchPopup() {
    const searchBox = document.getElementById('popup-search');
    const searchTerm = searchBox.value;
    searchBox.insertAdjacentHTML('afterend', '<div class="loading"></div>');
    setTimeout(() => {
        const loadingEl = document.querySelector('.loading');
        if (loadingEl) loadingEl.remove();
        showNotification("מחפש בתוך המחשב: " + searchTerm);
    },1000);
}

function addButtonRippleEffect() {
    document.querySelectorAll('button').forEach(button => {
        button.addEventListener('click', e => {
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');
            button.appendChild(ripple);
            const rect = button.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            setTimeout(() => ripple.remove(), 600);
        });
    });
}

function goToStats() {
    window.location.href = 'stats.html';
}

function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;
    document.body.appendChild(notification);
    setTimeout(() => {
        notification.classList.add('show');
    }, 100);
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 500);
    }, 3000);
}

function addUser() {
    const userName = prompt("הכנס שם משתמש:");
    if (userName) {
        const userTable = document.getElementById('user-table');
        const newRow = userTable.insertRow();
        const cell1 = newRow.insertCell(0);
        const cell2 = newRow.insertCell(1);
        cell1.textContent = userName;
        cell2.innerHTML = '<button onclick="removeUser(this)">הסר</button>';
        showNotification("משתמש נוסף בהצלחה!");
    }
}

function removeUser(button) {
    const row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
    showNotification("משתמש הוסר בהצלחה!");
}

document.addEventListener('DOMContentLoaded', addButtonRippleEffect);

window.onclick = function(e) {
    const popup = document.getElementById('popup');
    if (e.target == popup) closePopup();
};

let settings = {
    autoRefresh: true,
    notificationsEnabled: true,
    updateInterval: 5000
};

function openSettings() {
    document.getElementById('settingsPanel').classList.add('open');
}

function toggleAutoRefresh() {
    settings.autoRefresh = !settings.autoRefresh;
    showAlert(`רענון אוטומטי ${settings.autoRefresh ? 'הופעל' : 'כובה'}`);
}

function toggleNotifications() {
    settings.notificationsEnabled = !settings.notificationsEnabled;
    showAlert(`התראות ${settings.notificationsEnabled ? 'הופעלו' : 'כובו'}`);
}

function changeUpdateInterval(interval) {
    settings.updateInterval = parseInt(interval);
    showAlert(`תדירות העדכון שונתה ל-${interval/1000} שניות`);
}

function showAlert(message) {
    const alert = document.getElementById('alertBox');
    alert.textContent = message;
    alert.classList.add('show');
    setTimeout(() => alert.classList.remove('show'), 3000);
}

// Initialize dark mode from localStorage
document.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
    }
});
