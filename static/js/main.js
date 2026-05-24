// main.js - Enhanced with project modal functionality
document.addEventListener('DOMContentLoaded', function() {
    initializeProjectInteractions();
    initializeTimelineAnimations();
    initializeTechStackInteractions();
});

// Initialize all project-related interactions
function initializeProjectInteractions() {
    // Add click handlers to project cards
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach(card => {
        card.addEventListener('click', function(e) {
            // Don't trigger if clicking on links
            if (!e.target.closest('a')) {
                const projectId = this.dataset.projectId;
                if (projectId) {
                    showProjectDetails(projectId);
                }
            }
        });
    });

    // Add hover effects for project links in timeline
    const timelineProjectLinks = document.querySelectorAll('.timeline-item .btn-outline-primary');
    timelineProjectLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            const timelineItem = this.closest('.timeline-item');
            timelineItem.style.transform = 'scale(1.10)';
        });
        
        link.addEventListener('mouseleave', function() {
            const timelineItem = this.closest('.timeline-item');
            timelineItem.style.transform = 'scale(1)';
        });
    });
}

// Initialize timeline scroll animations
function initializeTimelineAnimations() {
    const timelineItems = document.querySelectorAll('.timeline-item');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, { threshold: 0.1 });

    timelineItems.forEach(item => {
        observer.observe(item);
    });
}

// Initialize tech stack interactions
function initializeTechStackInteractions() {
    // Add tooltips to tech stack badges
    const techBadges = document.querySelectorAll('.tech-stack .badge');
    techBadges.forEach(badge => {
        badge.setAttribute('title', `Click to filter ${badge.textContent} projects`);
        badge.style.cursor = 'pointer';
        
        badge.addEventListener('click', function() {
            const tech = this.textContent.trim();
            filterProjectsByTech(tech);
        });
    });
}

// Filter projects by technology
function filterProjectsByTech(technology) {
    const projectCards = document.querySelectorAll('.project-card');
    let visibleCount = 0;

    projectCards.forEach(card => {
        const techStack = card.querySelector('.tech-stack');
        const hasTech = techStack.textContent.includes(technology);
        
        if (hasTech) {
            card.style.display = 'block';
            card.style.animation = 'bounceIn 0.6s ease';
            visibleCount++;
        } else {
            card.style.display = 'none';
        }
    });

    // Show message if no projects found
    showFilterMessage(visibleCount, technology);
}

function showFilterMessage(count, tech) {
    // Remove existing message
    const existingMessage = document.querySelector('.filter-message');
    if (existingMessage) {
        existingMessage.remove();
    }

    if (count === 0) {
        const message = document.createElement('div');
        message.className = 'alert alert-info filter-message text-center mt-3';
        message.innerHTML = `
            No projects found with technology: <strong>${tech}</strong>. 
            <a href="#" class="alert-link" onclick="clearTechFilter()">Show all projects</a>
        `;
        document.querySelector('#projects').prepend(message);
    }
}

function clearTechFilter() {
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach(card => {
        card.style.display = 'block';
        card.style.animation = 'fadeIn 0.5s ease';
    });

    const message = document.querySelector('.filter-message');
    if (message) {
        message.remove();
    }
}

// Enhanced project detail modal (for future implementation)
function showProjectDetails(projectId) {
    // This would typically fetch project details via AJAX
    // For now, we'll use the existing page navigation
    console.log('Showing details for project:', projectId);
    
    // You can enhance this to show a modal instead of navigating
    // window.location.href = `/projects/${projectId}`;
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes bounceIn {
        0% { transform: scale(0.3); opacity: 0; }
        50% { transform: scale(1.05); opacity: 0.9; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    .project-card {
        animation: fadeIn 0.5s ease;
    }
`;
document.head.appendChild(style);