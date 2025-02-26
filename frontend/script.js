const API_URL = 'http://127.0.0.1:5000/api';

const computersContainer = document.getElementById('computer-list');

const computers = new Map();

// נתוני בדיקה
const testComputers = [
    {
        name: "מחשב-בדיקה-1",
        ip: "192.168.1.101",
        location: "חדר פיתוח",
        status: "פעיל",
        lastActive: new Date().toLocaleString(),
        keystrokes: [
            {
                window: "Visual Studio Code",
                timestamp: new Date().toISOString(),
                keystroke: "פיתוח מודול חדש למערכת"
            },
            {
                window: "Chrome",
                timestamp: new Date(Date.now() - 1500000).toISOString(),
                keystroke: "חיפוש פתרונות בגוגל"
            }
        ]
    },
    {
        name: "מחשב-בדיקה-2",
        ip: "192.168.1.102",
        location: "חדר בדיקות",
        status: "פעיל",
        lastActive: new Date().toLocaleString(),
        keystrokes: [
            {
                window: "Microsoft Word",
                timestamp: new Date().toISOString(),
                keystroke: "כתיבת מסמך אפיון"
            },
            {
                window: "Teams",
                timestamp: new Date(Date.now() - 3600000).toISOString(),
                keystroke: "פגישת צוות שבועית"
            }
        ]
    }
];

// Initialize event listeners
document.addEventListener('DOMContentLoaded', () => {
    // אתחול ראשוני
    initializeApp();
    
    // הוספת מאזינים לחיפוש
    setupSearchListeners();
});

function initializeApp() {
    document.getElementById('computer-list').innerHTML = '';
    
    testComputers.forEach(computer => {
        computers.set(computer.name, computer);
        addComputerToList(computer);
    });

    initDatePickers();
}

function setupSearchListeners() {
    // חיפוש גלובלי
    ['window-filter', 'content-filter'].forEach(id => {
        const input = document.getElementById(id);
        input.addEventListener('keyup', (e) => {
            if (e.key === 'Enter') search(true);
        });
    });

    // חיפוש במחשב ספציפי
    ['computer-window-filter', 'computer-content-filter'].forEach(id => {
        const input = document.getElementById(id);
        input.addEventListener('keyup', (e) => {
            if (e.key === 'Enter') searchComputerData(true);
        });
    });

    // מעקב אחרי שינוי תאריכים
    ['start-date', 'end-date'].forEach(id => {
        const input = document.getElementById(id);
        input.addEventListener('change', () => search(true));
    });

    // הוספת מאזיני לחיצה לאייקוני לוח השנה
    document.querySelectorAll('.calendar-trigger').forEach(icon => {
        icon.addEventListener('click', (e) => {
            const input = e.target.previousElementSibling;
            if (input && input.type === 'datetime-local') {
                input.showPicker();
            }
        });
    });
}

// פונקציות עזר
function addComputerToList(computer) {
    const computerElement = document.createElement('div');
    computerElement.className = 'computer';
    computerElement.innerHTML = `
        <i class="fas fa-laptop"></i>
        <span>${computer.name}</span>
        <div class="computer-status">${computer.status}</div>
    `;
    computerElement.onclick = () => showComputerDetails(computer.name);
    document.getElementById('computer-list').appendChild(computerElement);
}

function showComputerDetails(computerName) {
    const computer = computers.get(computerName);
    if (!computer) return;

    document.getElementById('computer-name-title').textContent = computer.name;
    
    const computerInfo = document.querySelector('.computer-info');
    computerInfo.innerHTML = `
        <p><strong>שם:</strong> ${computer.name}</p>
        <p><strong>IP:</strong> ${computer.ip}</p>
        <p><strong>מיקום:</strong> ${computer.location}</p>
        <p><strong>סטטוס:</strong> ${computer.status}</p>
        <p><strong>פעילות:</strong> ${computer.lastActive}</p>
    `;
    
    showComputerKeystrokes(computer);
    document.getElementById('computer-details-popup').style.display = 'block';
}

function showComputerKeystrokes(computer) {
    if (!computer.keystrokes) return;
    
    const container = document.getElementById('computer-search-results');
    container.innerHTML = '';
    
    computer.keystrokes.forEach(entry => {
        const div = document.createElement('div');
        div.className = 'keystroke-entry';
        div.innerHTML = `
            <div class="keystroke-window">${entry.window}</div>
            <div class="keystroke-time">${new Date(entry.timestamp).toLocaleString()}</div>
            <div class="keystroke-data">${entry.keystroke}</div>
        `;
        container.appendChild(div);
    });
}

// פונקציות חיפוש
// פונקציית חיפוש גלובלית מעודכנת
function search(isButtonClick = false) {
    const windowText = document.getElementById('window-filter').value.toLowerCase();
    const contentText = document.getElementById('content-filter').value.toLowerCase();
    const startDate = new Date(document.getElementById('start-date').value || '1970-01-01');
    const endDate = new Date(document.getElementById('end-date').value || '2100-01-01');

    const results = Array.from(computers.values())
        .flatMap(computer => computer.keystrokes
            .filter(entry => {
                const entryDate = new Date(entry.timestamp);
                return (!windowText || entry.window.toLowerCase().includes(windowText)) &&
                       (!contentText || entry.keystroke.toLowerCase().includes(contentText)) &&
                       entryDate >= startDate && entryDate <= endDate;
            })
            .map(entry => ({
                computerName: computer.name,
                ...entry
            }))
        );

    displaySearchResults(results);
}

function searchComputerData(isButtonClick = false) {
    const computerName = document.getElementById('computer-name-title').textContent;
    const computer = computers.get(computerName);
    if (!computer) return;

    const windowText = document.getElementById('computer-window-filter').value.toLowerCase();
    const contentText = document.getElementById('computer-content-filter').value.toLowerCase();
    const startDate = new Date(document.getElementById('computer-start-date').value || '1970-01-01');
    const endDate = new Date(document.getElementById('computer-end-date').value || '2100-01-01');

    const results = computer.keystrokes.filter(entry => {
        const entryDate = new Date(entry.timestamp);
        return (!windowText || entry.window.toLowerCase().includes(windowText)) &&
               (!contentText || entry.keystroke.toLowerCase().includes(contentText)) &&
               entryDate >= startDate && entryDate <= endDate;
    });

    displayComputerSearchResults(results);
}

function displaySearchResults(results) {
    const container = document.getElementById('search-results');
    container.innerHTML = '';
    
    if (results.length === 0) {
        container.innerHTML = '<div class="no-results">לא נמצאו תוצאות</div>';
    } else {
        results.forEach(entry => {
            const div = document.createElement('div');
            div.className = 'keystroke-entry';
            div.innerHTML = `
                <div class="keystroke-window">${entry.window}</div>
                <div class="keystroke-time">${new Date(entry.timestamp).toLocaleString()}</div>
                <div class="computer-name">מחשב: ${entry.computerName}</div>
                <div class="keystroke-data">${entry.keystroke}</div>
            `;
            container.appendChild(div);
        });
    }
    
    // הצגת הפופ-אפ
    document.getElementById('search-results-popup').style.display = 'block';
}

function displayComputerSearchResults(results) {
    const container = document.getElementById('computer-search-results');
    container.innerHTML = '';
    
    if (results.length === 0) {
        container.innerHTML = '<div class="no-results">לא נמצאו תוצאות</div>';
    } else {
        results.forEach(entry => {
            const div = document.createElement('div');
            div.className = 'keystroke-entry';
            div.innerHTML = `
                <div class="keystroke-window">${entry.window}</div>
                <div class="keystroke-time">${new Date(entry.timestamp).toLocaleString()}</div>
                <div class="keystroke-data">${entry.keystroke}</div>
            `;
            container.appendChild(div);
        });
    }
}

// פונקציות תאריכים
function initDatePickers() {
    const now = new Date();
    ['start-date', 'end-date', 'computer-start-date', 'computer-end-date'].forEach(id => {
        const picker = document.getElementById(id);
        if (picker) picker.valueAsDate = now;
    });
}

// פונקציות סגירה
function closeComputerDetails() {
    document.getElementById('computer-details-popup').style.display = 'none';
}

function closeSearchResults() {
    document.getElementById('search-results-popup').style.display = 'none';
}
