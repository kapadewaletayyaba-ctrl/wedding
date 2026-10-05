/* ==========================================================================
   EVERAFTER WEDDING PLANNER — INTERACTIVITY & APP LOGIC
   ========================================================================== */

// 1. Page Navigation Switcher
function switchPage(pageId) {
  // Hide all page sections
  const sections = document.querySelectorAll('.page-section');
  sections.forEach(section => section.classList.remove('active'));

  // Remove active highlight from navigation links
  const navLinks = document.querySelectorAll('.nav-links a');
  navLinks.forEach(link => link.classList.remove('active'));

  // Display targeted section
  const targetSection = document.getElementById('page-' + pageId);
  if (targetSection) {
    targetSection.classList.add('active');
  }

  // Set active highlight on active navigation link
  const targetNav = document.getElementById('nav-' + pageId);
  if (targetNav) {
    targetNav.classList.add('active');
  }

  // Smooth scroll back to top on view change
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// 2. Modal Window Controllers
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.add('active');
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.remove('active');
  }
}

// Close active modal when clicking outside content area
window.addEventListener('click', function(event) {
  if (event.target.classList.contains('modal')) {
    event.target.classList.remove('active');
  }
});

// 3. Live Countdown Timer Functionality
function startCountdown() {
  // Target Wedding Date
  const weddingDate = new Date('August 22, 2027 16:30:00').getTime();

  function updateTimer() {
    const now = new Date().getTime();
    const distance = weddingDate - now;

    if (distance < 0) {
      document.querySelector('.countdown-timer').innerHTML = "<h3>The Big Day is Here!</h3>";
      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    const timerBlocks = document.querySelectorAll('.countdown-timer .time-block span');
    if (timerBlocks.length === 4) {
      timerBlocks[0].innerText = days;
      timerBlocks[1].innerText = hours;
      timerBlocks[2].innerText = minutes;
      timerBlocks[3].innerText = seconds;
    }
  }

  updateTimer();
  setInterval(updateTimer, 1000);
}

// 4. Interactive Checklist Progress Updates
function initChecklistListeners() {
  const checkboxes = document.querySelectorAll('.checklist-item input[type="checkbox"]');
  checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
      const parent = this.closest('.checklist-item');
      if (parent) {
        if (this.checked) {
          parent.style.textDecoration = 'line-through';
          parent.style.opacity = '0.6';
        } else {
          parent.style.textDecoration = 'none';
          parent.style.opacity = '1';
        }
      }
    });
  });
}

// Initialize on DOM Load
document.addEventListener('DOMContentLoaded', () => {
  startCountdown();
  initChecklistListeners();
});