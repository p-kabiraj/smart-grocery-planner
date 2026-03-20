document.addEventListener('DOMContentLoaded', () => {
    // 1. Navigation Logic
    const navItems = document.querySelectorAll('.nav-item');
    const sections = document.querySelectorAll('.page-section');

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            // UI Update
            navItems.forEach(i => i.classList.remove('active'));
            sections.forEach(s => s.classList.remove('active'));

            item.classList.add('active');
            const target = item.getAttribute('data-target');
            document.getElementById(target).classList.add('active');
        });
    });

    // 2. Initialize Charts
    renderCharts();
});

function renderCharts() {
    // Spending Line Chart
    const ctx1 = document.getElementById('spendingChart').getContext('2d');
    new Chart(ctx1, {
        type: 'line',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'Spending ($)',
                data: [45, 52, 38, 65, 48, 70, 42],
                borderColor: '#4ade80',
                backgroundColor: 'rgba(74, 222, 128, 0.1)',
                fill: true,
                tension: 0.4
            }]
        },
        options: { responsive: true, plugins: { legend: { display: false } } }
    });

    // Category Pie Chart
    const ctx2 = document.getElementById('categoryChart').getContext('2d');
    new Chart(ctx2, {
        type: 'doughnut',
        data: {
            labels: ['Produce', 'Dairy', 'Meat', 'Pantry'],
            datasets: [{
                data: [35, 20, 25, 20],
                backgroundColor: ['#4ade80', '#38bdf8', '#fb923c', '#a78bfa'],
                borderWidth: 0
            }]
        }
    });
}

// 3. Grocery List Function
function addItem() {
    const input = document.getElementById('itemInput');
    const list = document.getElementById('grocery-list-items');
    if (input.value) {
        const li = document.createElement('li');
        li.className = 'list-item';
        li.innerHTML = `<span>${input.value}</span><button onclick="this.parentElement.remove()">✕</button>`;
        list.appendChild(li);
        input.value = "";
    }
}

// 4. PriceWise Comparison Logic
function runComparison() {
    const product = document.getElementById('compareSearch').value;
    const container = document.getElementById('comparison-results');

    if (!product) return alert("Enter a product name!");

    container.innerHTML = `<p style="color: #4ade80">Scanning partners for ${product}...</p>`;

    setTimeout(() => {
        const providers = [
            { name: 'Blinkit', price: (Math.random() * 40 + 5).toFixed(2), time: '12 min', status: 'Cheapest' },
            { name: 'Zepto', price: (Math.random() * 40 + 5).toFixed(2), time: '8 min', status: 'Fastest' },
            { name: 'Big Basket', price: (Math.random() * 40 + 5).toFixed(2), time: '25 min', status: 'Wide Range' }
        ];

        let html = `
            <table class="results-table">
                <thead><tr><th>App</th><th>Price</th><th>Delivery</th><th>Note</th></tr></thead>
                <tbody>
        `;
        
        providers.forEach(p => {
            html += `
                <tr>
                    <td><b>${p.name}</b></td>
                    <td>$${p.price}</td>
                    <td>${p.time}</td>
                    <td><span class="tag">${p.status}</span></td>
                </tr>`;
        });

        html += `</tbody></table>`;
        container.innerHTML = html;
    }, 1000);
}