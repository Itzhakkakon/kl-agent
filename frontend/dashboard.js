class Dashboard {
    constructor() {
        this.activeUsers = new Set();
        this.keyloggerData = new Map();
        this.initializeRealTimeUpdates();
    }

    initializeRealTimeUpdates() {
        setInterval(() => {
            this.updateActiveUsers();
            this.updateKeyloggerStats();
        }, 5000);
    }

    updateActiveUsers() {
        const count = Math.floor(Math.random() * 5) + 1;
        document.getElementById('active-users').textContent = count;
    }

    updateKeyloggerStats() {
        const computers = document.querySelectorAll('.computer');
        computers.forEach(computer => {
            const id = computer.dataset.id;
            const keyCount = Math.floor(Math.random() * 1000);
            const activityLevel = this.calculateActivityLevel(keyCount);
            this.updateComputerUI(computer, keyCount, activityLevel);
        });
    }

    updateComputerUI(computer, keyCount, activityLevel) {
        // עדכון ממשק המשתמש של המחשב
        if (!computer.querySelector('.activity-bar')) {
            this.addActivityBarToComputer(computer);
        }
        computer.querySelector('.activity-level').style.width = `${activityLevel}%`;
        computer.querySelector('.key-count').textContent = `הקשות: ${keyCount}`;
    }

    addActivityBarToComputer(computer) {
        // הוספת סרגל פעילות למחשב
        const activityBar = document.createElement('div');
        activityBar.className = 'activity-bar';
        activityBar.innerHTML = `
            <div class="activity-level"></div>
            <div class="key-count">0</div>
        `;
        computer.appendChild(activityBar);
    }

    calculateActivityLevel(keyCount) {
        return Math.min((keyCount / 1000) * 100, 100);
    }

    exportData(format = 'json') {
        const data = {
            timestamp: new Date().toISOString(),
            computers: Array.from(this.keyloggerData.entries())
        };
        return format === 'json' ? JSON.stringify(data, null, 2) : this.convertToCSV(data);
    }

    convertToCSV(data) {
        return 'timestamp,computer,keyCount\n' + 
               data.computers.map(([pc, count]) => 
                   `${data.timestamp},${pc},${count}`
               ).join('\n');
    }
}

// יצירת מופע חדש של הדשבורד
const dashboard = new Dashboard();

// פונקציות עזר גלובליות
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
}

function exportLogs(format) {
    const data = dashboard.exportData(format);
    const blob = new Blob([data], { type: 'text/plain' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `keylogger-data.${format}`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
}

// אתחול הדשבורד כשהדף נטען
document.addEventListener('DOMContentLoaded', () => {
    dashboard.updateActiveUsers();
    dashboard.updateKeyloggerStats();
});
