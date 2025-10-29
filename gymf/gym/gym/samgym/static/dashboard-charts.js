document.addEventListener('DOMContentLoaded', function() {
    // Toggle sidebar
    const menuToggle = document.querySelector('.menu-toggle');
    const sidebar = document.querySelector('.sidebar');
    
    menuToggle.addEventListener('click', function() {
        sidebar.classList.toggle('collapsed');
    });
    
    // Initialize charts
    const membershipCtx = document.getElementById('membershipChart').getContext('2d');
    const attendanceCtx = document.getElementById('attendanceChart').getContext('2d');
    
    // Membership Growth Chart
    const membershipChart = new Chart(membershipCtx, {
        type: 'line',
        data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
                label: 'New Members',
                data: [45, 60, 75, 82, 78, 92, 105, 120, 110, 95, 130, 150],
                backgroundColor: 'rgba(255, 107, 107, 0.2)',
                borderColor: 'rgba(255, 107, 107, 1)',
                borderWidth: 2,
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
    
    // Attendance Trend Chart
    const attendanceChart = new Chart(attendanceCtx, {
        type: 'bar',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            datasets: [{
                label: 'Check-ins',
                data: [120, 150, 180, 140, 160, 90, 70],
                backgroundColor: 'rgba(78, 205, 196, 0.8)',
                borderColor: 'rgba(78, 205, 196, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                },
                x: {
                    grid: {
                        display: false
                    }
                }
            }
        }
    });
    
    // Filter charts when dropdown changes
    document.querySelectorAll('.chart-filter').forEach(filter => {
        filter.addEventListener('change', function() {
            // In a real app, you would fetch new data based on the filter
            console.log('Filter changed to:', this.value);
        });
    });
});