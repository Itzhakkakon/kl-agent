const API_URL = 'http://127.0.0.1:5000/api';

const computersContainer = document.getElementById('computer-list');



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
    const computer = computers.get(computerName) || {
        name: computerName,
        ip: 'לא זמין',
        location: 'לא זמין'
    };

    document.getElementById("popup-title").innerText = "אפשרויות עבור " + computerName;
    document.getElementById("computer-details").innerHTML = `
        <div class="computer-info">
            <p><strong>שם מחשב:</strong> ${computer.name}</p>
            <p><strong>כתובת IP:</strong> ${computer.ip}</p>
            <p><strong>מיקום:</strong> ${computer.location}</p>
        </div>
    `;
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
    fetchComputerDetails(query);
}



// Fix gauge initialization - make sure it runs after DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const gaugeElement = document.getElementById('activity-gauge');
    if (gaugeElement) {
        const gauge = new Gauge(gaugeElement);
        gauge.maxValue = 24;
        gauge.setMinValue(0);
        gauge.animationSpeed = 32;
        gauge.set(0);
        
        // Configure gauge appearance
        gauge.setOptions({
            angle: -0.2,
            lineWidth: 0.2,
            radiusScale: 0.9,
            pointer: {
                length: 0.6,
                strokeWidth: 0.035,
                color: '#00ff00'
            },
            limitMax: false,
            limitMin: false,
            colorStart: '#6FADCF',
            colorStop: '#8FC0DA',
            strokeColor: '#E0E0E0',
            generateGradient: true,
            highDpiSupport: true,
            percentColors: [[0.0, "#a9d70b"], [0.50, "#f9c802"], [1.0, "#ff0000"]]
        });

        // Update gauge every minute
        setInterval(() => {
            let currentValue = parseFloat(document.getElementById('active-time').textContent);
            if (currentValue < 24) {
                currentValue += 0.1;
                document.getElementById('active-time').textContent = currentValue.toFixed(1);
                gauge.set(currentValue);
            }
        }, 60000);
    }
});

function openAddComputerPopup() {
    document.getElementById('add-computer-popup').style.display = 'block';
}

function closeAddComputerPopup() {
    document.getElementById('add-computer-popup').style.display = 'none';
}

// Add computer storage
const computers = new Map();

// Fix computer addition functionality
document.getElementById('add-computer-form').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const computerName = document.getElementById('computer-name').value;
    const computerIP = document.getElementById('computer-ip').value;
    const computerLocation = document.getElementById('computer-location').value;

    // Store computer details
    computers.set(computerName, {
        name: computerName,
        ip: computerIP,
        location: computerLocation
    });

    // Create new computer element
    const computerList = document.querySelector('.computer-list');
    const newComputer = document.createElement('div');
    newComputer.className = 'computer';
    newComputer.innerHTML = `
        <i class="fas fa-laptop"></i>
        <span>${computerName}</span>
    `;
    
    // Add click handler
    newComputer.addEventListener('click', () => openPopup(computerName));
    
    // Add to list
    computerList.appendChild(newComputer);

    // Update counter
    const countElement = document.getElementById('computer-count');
    const currentCount = parseInt(countElement.textContent);
    countElement.textContent = currentCount + 1;

    // Clear and close form
    document.getElementById('add-computer-form').reset();
    closeAddComputerPopup();
});

// UI Rendering Functions
function renderComputersList(computers) {
    computersContainer.innerHTML = '';
    
    if (computers.length === 0) {
        computersContainer.innerHTML = '<p>לא נמצאו מחשבים</p>';
        return;
    }
    
    computers.forEach(computer => {
        const computerElement = document.createElement('div');
        computerElement.onclick =() => openPopup(computer)
        computerElement.className = 'computer';
        computerElement.innerHTML = `
            <i class="fas fa-laptop"></i>
            <span>${computer}</span>`
        
            computersContainer.appendChild(computerElement);
    });
}

// '/api/computers/<pc>', methods=['GET']

async function fetchComputerDetails(computer) {
    try {
        const response = await fetch(`${API_URL}/computers/${computer}`);
        const data = await response.json();
        
        if (response.ok) {
            alert(data[0]["data"]);
        } else {
            showError(student.error || 'שגיאה בטעינת פרטי המחשב');
        }
    } catch (error) {
        alert('שגיאה בטעינת פרטי המחשב');
        console.error('Error fetching computer details:', error);
    }
}

// API Functions
async function fetchComputer() {
    try {
        const response = await fetch(`${API_URL}/computers`);
        const computers = await response.json();
        renderComputersList(computers);
    } catch (error) {
        alert('שגיאה בטעינת רשימת המחשבים');
        console.error('Error fetching computers:', error);
    }
}

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    fetchComputer();
    setupEventListeners();
});
