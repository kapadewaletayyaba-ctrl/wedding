import streamlit as st
import streamlit.components.v1 as components
# Set Streamlit page configuration
st.set_page_config(
    page_title="Wedding Planner & Dashboard",
    page_icon="💍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Complete HTML/JS/CSS string
HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wedding Planner & Dashboard</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Great+Vibes&family=Montserrat:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        gold: {
                            DEFAULT: '#D4A574',
                            light: '#F3E5D8',
                            dark: '#B38453',
                            50: '#FAF4EE',
                            100: '#F5E8DC'
                        },
                        cream: {
                            DEFAULT: '#FDF6F0',
                            dark: '#F4ECE4',
                            light: '#FFFDFB'
                        },
                        rose: {
                            custom: '#E85D7A',
                            light: '#F8D7DF',
                            dark: '#C43A57'
                        },
                        charcoal: {
                            DEFAULT: '#2C2A29',
                            light: '#5A5654',
                            muted: '#8C8783'
                        }
                    },
                    fontFamily: {
                        serif: ['Playfair Display', 'serif'],
                        accent: ['Great Vibes', 'cursive'],
                        sans: ['Montserrat', 'sans-serif'],
                        garamond: ['Cormorant Garamond', 'serif']
                    },
                    boxShadow: {
                        'soft': '0 10px 30px -10px rgba(212, 165, 116, 0.2)',
                        'gold-glow': '0 0 20px rgba(212, 165, 116, 0.35)',
                        'card': '0 4px 20px rgba(0, 0, 0, 0.04)'
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background-color: #FDF6F0;
            color: #2C2A29;
            font-family: 'Montserrat', sans-serif;
            overflow-x: hidden;
            margin: 0;
            padding: 0;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(212, 165, 116, 0.25);
        }
        .glass-dark {
            background: rgba(44, 42, 41, 0.85);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(212, 165, 116, 0.3);
        }
        .gold-gradient-text {
            background: linear-gradient(135deg, #B38453 0%, #D4A574 50%, #E6C59E 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .gold-gradient-bg {
            background: linear-gradient(135deg, #D4A574 0%, #C3925F 100%);
        }
        .gold-gradient-bg:hover {
            background: linear-gradient(135deg, #C3925F 0%, #B38453 100%);
        }
        .custom-scrollbar::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: #FDF6F0;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #D4A574;
            border-radius: 4px;
        }
        .nav-link.active {
            color: #D4A574;
            border-bottom: 2px solid #D4A574;
            font-weight: 600;
        }
        .page-view {
            transition: opacity 0.3s ease-in-out, transform 0.3s ease-in-out;
        }
        .page-view.hidden {
            display: none !important;
            opacity: 0;
            transform: translateY(10px);
        }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between custom-scrollbar">

    <!-- Top Navigation Header -->
    <header class="sticky top-0 z-40 bg-white/90 backdrop-blur-md border-b border-gold/20 shadow-sm transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-20">
                <!-- Brand Logo -->
                <div class="flex items-center space-x-3 cursor-pointer" onclick="navigateTo('home')">
                    <div class="w-10 h-10 rounded-full border-2 border-gold flex items-center justify-center bg-gold-50 shadow-sm">
                        <i class="fa-solid font-accent text-2xl text-gold">E</i>
                    </div>
                    <div>
                        <span class="font-serif text-2xl tracking-wide font-bold text-charcoal block leading-none">WedPlanner</span>
                        <span class="font-accent text-sm text-gold block tracking-widest leading-none mt-1">Wedding Couture & Planning</span>
                    </div>
                </div>

                <!-- Desktop Navigation Links -->
                <nav class="hidden lg:flex items-center space-x-6 text-sm font-medium">
                    <button onclick="navigateTo('home')" id="nav-home" class="nav-link active py-2 text-charcoal hover:text-gold transition">Home</button>
                    <button onclick="navigateTo('dashboard')" id="nav-dashboard" class="nav-link py-2 text-charcoal hover:text-gold transition">Dashboard</button>
                    <button onclick="navigateTo('budget')" id="nav-budget" class="nav-link py-2 text-charcoal hover:text-gold transition">Budget</button>
                    <button onclick="navigateTo('vendors')" id="nav-vendors" class="nav-link py-2 text-charcoal hover:text-gold transition">Vendors</button>
                    <button onclick="navigateTo('guests')" id="nav-guests" class="nav-link py-2 text-charcoal hover:text-gold transition">Guests</button>
                    <button onclick="navigateTo('checklist')" id="nav-checklist" class="nav-link py-2 text-charcoal hover:text-gold transition">Checklist</button>
                    <button onclick="navigateTo('timeline')" id="nav-timeline" class="nav-link py-2 text-charcoal hover:text-gold transition">Timeline</button>
                    <button onclick="navigateTo('messages')" id="nav-messages" class="nav-link py-2 text-charcoal hover:text-gold transition relative">
                        Messages
                        <span id="unread-msg-badge" class="absolute -top-1 -right-2 bg-rose-custom text-white text-[10px] w-4 h-4 rounded-full flex items-center justify-center">2</span>
                    </button>
                </nav>

                <!-- Action Controls & Auth State -->
                <div class="hidden sm:flex items-center space-x-4">
                    <div id="user-auth-badge" class="flex items-center space-x-3 bg-cream p-1.5 pr-4 rounded-full border border-gold/30">
                        <img id="user-avatar" src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80" alt="Sophia & Alexander" class="w-8 h-8 rounded-full object-cover border border-gold">
                        <div class="text-left leading-tight">
                            <span id="user-display-name" class="font-semibold text-xs text-charcoal block">Sophia & Alex</span>
                            <span class="text-[10px] text-gold-dark font-medium">Jun 18, 2027</span>
                        </div>
                    </div>
                </div>

                <!-- Mobile Navigation Menu Toggle -->
                <div class="flex lg:hidden items-center space-x-2">
                    <button onclick="toggleMobileMenu()" class="p-2 text-charcoal hover:text-gold focus:outline-none">
                        <i class="fa-solid fa-bars text-xl"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Drawer Menu -->
        <div id="mobile-menu" class="hidden lg:hidden bg-white border-b border-gold/20 px-4 pt-2 pb-6 space-y-2 shadow-lg">
            <button onclick="navigateTo('home'); toggleMobileMenu();" class="block w-full text-left py-2 px-3 text-sm font-medium hover:bg-cream rounded-lg">Home</button>
            <button onclick="navigateTo('dashboard'); toggleMobileMenu();" class="block w-full text-left py-2 px-3 text-sm font-medium hover:bg-cream rounded-lg">Dashboard</button>
            <button onclick="navigateTo('budget'); toggleMobileMenu();" class="block w-full text-left py-2 px-3 text-sm font-medium hover:bg-cream rounded-lg">Budget Planner</button>
            <button onclick="navigateTo('vendors'); toggleMobileMenu();" class="block w-full text-left py-2 px-3 text-sm font-medium hover:bg-cream rounded-lg">Vendor Directory</button>
            <button onclick="navigateTo('guests'); toggleMobileMenu();" class="block w-full text-left py-2 px-3 text-sm font-medium hover:bg-cream rounded-lg">Guest List</button>
            <button onclick="navigateTo('checklist'); toggleMobileMenu();" class="block w-full text-left py-2 px-3 text-sm font-medium hover:bg-cream rounded-lg">Wedding Checklist</button>
            <button onclick="navigateTo('timeline'); toggleMobileMenu();" class="block w-full text-left py-2 px-3 text-sm font-medium hover:bg-cream rounded-lg">Timeline & Countdown</button>
            <button onclick="navigateTo('messages'); toggleMobileMenu();" class="block w-full text-left py-2 px-3 text-sm font-medium hover:bg-cream rounded-lg">Messages Board</button>
        </div>
    </header>

    <!-- Toast Notification Container -->
    <div id="toast-container" class="fixed bottom-5 right-5 z-50 flex flex-col space-y-2 pointer-events-none"></div>

    <!-- MAIN CONTENT SPA VIEWS -->
    <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">

        <!-- VIEW 1: HOME PAGE -->
        <section id="view-home" class="page-view space-y-16">
            <div class="relative rounded-3xl overflow-hidden shadow-2xl min-h-[520px] flex items-center justify-center text-center p-8 bg-cover bg-center" style="background-image: linear-gradient(rgba(44, 42, 41, 0.45), rgba(44, 42, 41, 0.65)), url('https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=1600&q=80');">
                <div class="max-w-3xl space-y-6 text-white z-10 animate-fade-in">
                    <span class="inline-block font-accent text-3xl sm:text-4xl text-gold-light tracking-wide">Crafting Your Dream Celebration</span>
                    <h1 class="font-serif text-4xl sm:text-6xl font-bold leading-tight">Elegance, Magic & Perfect Memories</h1>
                    <p class="font-sans text-sm sm:text-lg text-gray-100 max-w-2xl mx-auto font-light leading-relaxed">
                        Organize every detail of your special day seamlessly with intuitive budget tracking, guest management, curating premier vendors, and dynamic day-of timelines.
                    </p>
                    <div class="flex flex-wrap justify-center gap-4 pt-4">
                        <button onclick="navigateTo('dashboard')" class="gold-gradient-bg text-white font-semibold px-8 py-3.5 rounded-full shadow-lg hover:shadow-gold-glow transition-all transform hover:-translate-y-0.5">
                            Start Planning Now <i class="fa-solid fa-arrow-right ml-2 text-xs"></i>
                        </button>
                        <button onclick="navigateTo('vendors')" class="bg-white/20 backdrop-blur-md text-white border border-white/40 font-semibold px-8 py-3.5 rounded-full hover:bg-white hover:text-charcoal transition-all">
                            Explore Featured Vendors
                        </button>
                    </div>
                </div>
            </div>

            <!-- Inspiration Gallery Grid -->
            <div class="space-y-6">
                <div class="text-center space-y-2">
                    <span class="font-accent text-2xl text-gold block">Visual Inspiration</span>
                    <h2 class="font-serif text-3xl sm:text-4xl font-bold text-charcoal">Wedding Gallery & Decor Ideas</h2>
                    <p class="text-charcoal-muted text-sm max-w-xl mx-auto">Explore handpicked romantic aesthetics, floral centerpieces, bridal attire, and luxury venue layouts.</p>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <div class="md:col-span-2 group relative h-80 rounded-2xl overflow-hidden shadow-card cursor-pointer" onclick="navigateTo('vendors')">
                        <img src="https://images.unsplash.com/photo-1519167758481-83f550bb49b3?auto=format&fit=crop&w=800&q=80" alt="Venue Inspiration" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                        <div class="absolute inset-0 bg-gradient-to-t from-charcoal/80 via-transparent to-transparent flex flex-col justify-end p-6 text-white">
                            <span class="text-xs uppercase tracking-widest text-gold font-semibold">Venues & Estates</span>
                            <h3 class="font-serif text-2xl font-bold">Grand Ballroom Elegance</h3>
                        </div>
                    </div>
                    <div class="group relative h-80 rounded-2xl overflow-hidden shadow-card cursor-pointer" onclick="navigateTo('vendors')">
                        <img src="https://images.unsplash.com/photo-1526047932273-341f2a7631f9?auto=format&fit=crop&w=800&q=80" alt="Floral Inspiration" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                        <div class="absolute inset-0 bg-gradient-to-t from-charcoal/80 via-transparent to-transparent flex flex-col justify-end p-4 text-white">
                            <span class="text-xs uppercase tracking-widest text-gold font-semibold">Florals</span>
                            <h3 class="font-serif text-xl font-bold">Pastel Rose & Eucalyptus</h3>
                        </div>
                    </div>
                    <div class="group relative h-80 rounded-2xl overflow-hidden shadow-card cursor-pointer" onclick="navigateTo('vendors')">
                        <img src="https://images.unsplash.com/photo-1537633552985-df8429e8048b?auto=format&fit=crop&w=800&q=80" alt="Photography" class="w-full h-full object-cover group-hover:scale-105 transition duration-500">
                        <div class="absolute inset-0 bg-gradient-to-t from-charcoal/80 via-transparent to-transparent flex flex-col justify-end p-4 text-white">
                            <span class="text-xs uppercase tracking-widest text-gold font-semibold">Moments</span>
                            <h3 class="font-serif text-xl font-bold">Sunset Couple Portraits</h3>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Featured Vendors Teaser -->
            <div class="space-y-6">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end gap-2">
                    <div>
                        <span class="font-accent text-2xl text-gold block">Handpicked Quality</span>
                        <h2 class="font-serif text-3xl font-bold text-charcoal">Featured Wedding Vendors</h2>
                    </div>
                    <button onclick="navigateTo('vendors')" class="text-gold-dark hover:text-gold font-semibold text-sm flex items-center gap-2">
                        View All Directory <i class="fa-solid fa-arrow-right text-xs"></i>
                    </button>
                </div>
                <div id="home-featured-vendors" class="grid grid-cols-1 md:grid-cols-3 gap-6"></div>
            </div>

            <!-- Testimonials -->
            <div class="bg-cream border border-gold/30 rounded-3xl p-8 sm:p-12 text-center space-y-6 relative overflow-hidden">
                <div class="absolute -top-10 -left-10 text-gold/10 text-9xl font-serif">“</div>
                <span class="font-accent text-3xl text-gold block">Real Love Stories</span>
                <h2 class="font-serif text-3xl sm:text-4xl font-bold text-charcoal">What Our Couples Say</h2>
                <div class="max-w-2xl mx-auto space-y-4">
                    <p class="font-serif italic text-lg sm:text-xl text-charcoal-light">
                        "WedPlanner made planning our 200-guest estate wedding completely stress-free. The real-time budget calculator, guest seating tracker, and direct messaging with our florist kept everything in perfect harmony!"
                    </p>
                    <div class="flex items-center justify-center space-x-3 pt-2">
                        <img src="https://images.unsplash.com/photo-1606800052052-a08af7148866?auto=format&fit=crop&w=200&q=80" alt="Couple" class="w-12 h-12 rounded-full object-cover border-2 border-gold">
                        <div class="text-left">
                            <h4 class="font-semibold text-sm text-charcoal">Claire & Jonathan Vance</h4>
                            <span class="text-xs text-gold-dark">Married in Tuscany, Italy</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- VIEW 2: DASHBOARD -->
        <section id="view-dashboard" class="page-view hidden space-y-8">
            <div class="bg-white rounded-3xl p-6 sm:p-8 border border-gold/30 shadow-card flex flex-col md:flex-row justify-between items-center gap-6">
                <div class="flex items-center space-x-4">
                    <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=200&q=80" alt="Sophia & Alexander" class="w-20 h-20 rounded-full object-cover border-2 border-gold shadow-md">
                    <div>
                        <div class="flex items-center space-x-2">
                            <h1 id="dashboard-couple-names" class="font-serif text-2xl sm:text-3xl font-bold text-charcoal">Sophia & Alexander</h1>
                        </div>
                        <p class="text-sm text-charcoal-muted mt-1"><i class="fa-solid fa-location-dot text-gold mr-1"></i> <span id="dashboard-location">The Grand Estate, Napa Valley</span></p>
                        <p class="text-xs text-gold-dark font-medium mt-1"><i class="fa-regular fa-calendar mr-1"></i> June 18, 2027</p>
                    </div>
                </div>
                <div class="flex flex-wrap items-center gap-3">
                    <div class="bg-gold-50 border border-gold/30 px-5 py-3 rounded-2xl text-center">
                        <span id="dash-countdown-days" class="font-serif text-2xl font-bold text-gold-dark block">256</span>
                        <span class="text-[11px] uppercase tracking-wider text-charcoal font-semibold">Days to Go</span>
                    </div>
                    <button onclick="navigateTo('budget')" class="gold-gradient-bg text-white px-5 py-3 rounded-xl font-semibold text-sm shadow-sm hover:shadow-md transition">
                        <i class="fa-solid fa-wallet mr-2"></i> Manage Budget
                    </button>
                </div>
            </div>

            <!-- Quick Metrics Grid -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                <div class="bg-white p-6 rounded-2xl border border-gold/20 shadow-card flex items-center justify-between">
                    <div>
                        <span class="text-xs text-charcoal-muted uppercase tracking-wider block font-medium">Total Budget</span>
                        <h3 id="stat-total-budget" class="font-serif text-2xl font-bold text-charcoal mt-1">$45,000</h3>
                        <span class="text-xs text-emerald-600 font-medium mt-1 inline-block"><i class="fa-solid fa-check mr-1"></i> On track</span>
                    </div>
                    <div class="w-12 h-12 rounded-xl bg-gold-50 flex items-center justify-center text-gold text-xl">
                        <i class="fa-solid fa-coins"></i>
                    </div>
                </div>
                <div class="bg-white p-6 rounded-2xl border border-gold/20 shadow-card flex items-center justify-between">
                    <div>
                        <span class="text-xs text-charcoal-muted uppercase tracking-wider block font-medium">Guest RSVPs</span>
                        <h3 id="stat-rsvp-count" class="font-serif text-2xl font-bold text-charcoal mt-1">118 / 150</h3>
                        <span class="text-xs text-gold-dark font-medium mt-1 inline-block">78.6% Confirmed</span>
                    </div>
                    <div class="w-12 h-12 rounded-xl bg-gold-50 flex items-center justify-center text-gold text-xl">
                        <i class="fa-solid fa-users"></i>
                    </div>
                </div>
                <div class="bg-white p-6 rounded-2xl border border-gold/20 shadow-card flex items-center justify-between">
                    <div>
                        <span class="text-xs text-charcoal-muted uppercase tracking-wider block font-medium">Vendors Booked</span>
                        <h3 id="stat-vendors-count" class="font-serif text-2xl font-bold text-charcoal mt-1">4 / 6</h3>
                        <span class="text-xs text-gold-dark font-medium mt-1 inline-block">2 pending contracts</span>
                    </div>
                    <div class="w-12 h-12 rounded-xl bg-gold-50 flex items-center justify-center text-gold text-xl">
                        <i class="fa-solid fa-handshake"></i>
                    </div>
                </div>
                <div class="bg-white p-6 rounded-2xl border border-gold/20 shadow-card flex items-center justify-between">
                    <div>
                        <span class="text-xs text-charcoal-muted uppercase tracking-wider block font-medium">Checklist Done</span>
                        <h3 id="stat-checklist-progress" class="font-serif text-2xl font-bold text-charcoal mt-1">12 / 18</h3>
                        <span class="text-xs text-gold-dark font-medium mt-1 inline-block">66% Completed</span>
                    </div>
                    <div class="w-12 h-12 rounded-xl bg-gold-50 flex items-center justify-center text-gold text-xl">
                        <i class="fa-solid fa-list-check"></i>
                    </div>
                </div>
            </div>

            <!-- Dashboard Action Hub & Quick Activity -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <div class="lg:col-span-2 bg-white rounded-3xl p-6 sm:p-8 border border-gold/20 shadow-card space-y-6">
                    <div class="flex justify-between items-center">
                        <h3 class="font-serif text-xl font-bold text-charcoal">Upcoming Milestone Deadlines</h3>
                        <button onclick="navigateTo('checklist')" class="text-xs text-gold-dark font-semibold hover:underline">View All Checklist</button>
                    </div>
                    <div id="dash-milestones-list" class="space-y-3"></div>
                </div>

                <div class="bg-white rounded-3xl p-6 sm:p-8 border border-gold/20 shadow-card space-y-6">
                    <h3 class="font-serif text-xl font-bold text-charcoal">Quick Actions</h3>
                    <div class="space-y-3">
                        <button onclick="navigateTo('budget')" class="w-full text-left p-3.5 rounded-xl border border-gold/20 hover:bg-gold-50 transition flex items-center justify-between text-sm font-medium text-charcoal">
                            <span><i class="fa-solid fa-plus-circle text-gold mr-2"></i> Add Expense Item</span>
                            <i class="fa-solid fa-chevron-right text-xs text-gold"></i>
                        </button>
                        <button onclick="navigateTo('guests')" class="w-full text-left p-3.5 rounded-xl border border-gold/20 hover:bg-gold-50 transition flex items-center justify-between text-sm font-medium text-charcoal">
                            <span><i class="fa-solid fa-user-plus text-gold mr-2"></i> Invite New Guest</span>
                            <i class="fa-solid fa-chevron-right text-xs text-gold"></i>
                        </button>
                        <button onclick="navigateTo('vendors')" class="w-full text-left p-3.5 rounded-xl border border-gold/20 hover:bg-gold-50 transition flex items-center justify-between text-sm font-medium text-charcoal">
                            <span><i class="fa-solid fa-magnifying-glass text-gold mr-2"></i> Browse Vendors</span>
                            <i class="fa-solid fa-chevron-right text-xs text-gold"></i>
                        </button>
                        <button onclick="navigateTo('messages')" class="w-full text-left p-3.5 rounded-xl border border-gold/20 hover:bg-gold-50 transition flex items-center justify-between text-sm font-medium text-charcoal">
                            <span><i class="fa-solid fa-message text-gold mr-2"></i> Open Messages</span>
                            <i class="fa-solid fa-chevron-right text-xs text-gold"></i>
                        </button>
                    </div>
                </div>
            </div>
        </section>

        <!-- VIEW 3: BUDGET PLANNER -->
        <section id="view-budget" class="page-view hidden space-y-8">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-white p-6 rounded-3xl border border-gold/30 shadow-card">
                <div>
                    <span class="font-accent text-2xl text-gold block">Financial Control</span>
                    <h1 class="font-serif text-3xl font-bold text-charcoal">Wedding Budget Planner</h1>
                </div>
                <div class="flex items-center gap-3">
                    <button onclick="openAddBudgetModal()" class="gold-gradient-bg text-white px-5 py-2.5 rounded-xl text-sm font-semibold shadow-sm hover:shadow-md transition">
                        <i class="fa-solid fa-plus mr-1"></i> Add Expense
                    </button>
                </div>
            </div>

            <!-- Budget Overview Cards -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-white p-6 rounded-2xl border border-gold/20 shadow-card">
                    <span class="text-xs text-charcoal-muted uppercase tracking-wider font-semibold">Total Allocated Budget</span>
                    <div class="flex items-baseline justify-between mt-2">
                        <h2 id="budget-total-display" class="font-serif text-3xl font-bold text-charcoal">$45,000</h2>
                    </div>
                </div>
                <div class="bg-white p-6 rounded-2xl border border-gold/20 shadow-card">
                    <span class="text-xs text-charcoal-muted uppercase tracking-wider font-semibold">Total Spent / Committed</span>
                    <h2 id="budget-spent-display" class="font-serif text-3xl font-bold text-charcoal mt-2">$32,450</h2>
                    <span id="budget-percent-display" class="text-xs text-gold-dark font-semibold mt-1 inline-block">72.1% of budget used</span>
                </div>
                <div class="bg-white p-6 rounded-2xl border border-gold/20 shadow-card">
                    <span class="text-xs text-charcoal-muted uppercase tracking-wider font-semibold">Remaining Funds</span>
                    <h2 id="budget-remaining-display" class="font-serif text-3xl font-bold text-emerald-600 mt-2">$12,550</h2>
                    <span class="text-xs text-charcoal-muted font-medium mt-1 inline-block">Available for extras</span>
                </div>
            </div>

            <!-- Expense Breakdown Table & Categories -->
            <div class="bg-white rounded-3xl p-6 sm:p-8 border border-gold/20 shadow-card space-y-6">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                    <h3 class="font-serif text-xl font-bold text-charcoal">Expense Categories & Items</h3>
                    <div class="flex items-center space-x-2 text-sm">
                        <span class="text-charcoal-muted">Filter by Category:</span>
                        <select id="budget-filter-category" onchange="renderBudgetTable()" class="bg-cream border border-gold/30 rounded-lg px-3 py-1.5 text-xs focus:outline-none">
                            <option value="ALL">All Categories</option>
                            <option value="Venue">Venue</option>
                            <option value="Catering">Catering</option>
                            <option value="Photography">Photography</option>
                            <option value="Attire & Beauty">Attire & Beauty</option>
                            <option value="Decor & Florals">Decor & Florals</option>
                            <option value="Entertainment">Entertainment</option>
                        </select>
                    </div>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr class="border-b border-gold/20 text-xs text-charcoal-muted uppercase tracking-wider">
                                <th class="py-3 px-4">Item Description</th>
                                <th class="py-3 px-4">Category</th>
                                <th class="py-3 px-4">Estimated ($)</th>
                                <th class="py-3 px-4">Actual ($)</th>
                                <th class="py-3 px-4">Status</th>
                                <th class="py-3 px-4 text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody id="budget-table-body" class="divide-y divide-gold/10 text-sm text-charcoal"></tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- VIEW 4: VENDOR DIRECTORY -->
        <section id="view-vendors" class="page-view hidden space-y-8">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-white p-6 rounded-3xl border border-gold/30 shadow-card">
                <div>
                    <span class="font-accent text-2xl text-gold block">Trusted Partners</span>
                    <h1 class="font-serif text-3xl font-bold text-charcoal">Vendor Directory & Management</h1>
                </div>
            </div>

            <div id="vendor-grid" class="grid grid-cols-1 md:grid-cols-3 gap-6"></div>
        </section>

        <!-- VIEW 5: GUEST LIST -->
        <section id="view-guests" class="page-view hidden space-y-8">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-white p-6 rounded-3xl border border-gold/30 shadow-card">
                <div>
                    <span class="font-accent text-2xl text-gold block">Invites & Seating</span>
                    <h1 class="font-serif text-3xl font-bold text-charcoal">Guest List Manager</h1>
                </div>
            </div>

            <div class="bg-white rounded-3xl p-6 sm:p-8 border border-gold/20 shadow-card space-y-6">
                <div class="overflow-x-auto">
                    <table class="w-full text-left border-collapse">
                        <thead>
                            <tr class="border-b border-gold/20 text-xs text-charcoal-muted uppercase tracking-wider">
                                <th class="py-3 px-4">Guest Name</th>
                                <th class="py-3 px-4">Category</th>
                                <th class="py-3 px-4">RSVP Status</th>
                                <th class="py-3 px-4">Dietary Needs</th>
                                <th class="py-3 px-4 text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody id="guest-table-body" class="divide-y divide-gold/10 text-sm text-charcoal"></tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- VIEW 6: CHECKLIST -->
        <section id="view-checklist" class="page-view hidden space-y-8">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-white p-6 rounded-3xl border border-gold/30 shadow-card">
                <div>
                    <span class="font-accent text-2xl text-gold block">Step by Step</span>
                    <h1 class="font-serif text-3xl font-bold text-charcoal">Wedding Checklist</h1>
                </div>
            </div>

            <div class="bg-white rounded-3xl p-6 sm:p-8 border border-gold/20 shadow-card space-y-4" id="checklist-container">
            </div>
        </section>

        <!-- VIEW 7: TIMELINE -->
        <section id="view-timeline" class="page-view hidden space-y-8">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-white p-6 rounded-3xl border border-gold/30 shadow-card">
                <div>
                    <span class="font-accent text-2xl text-gold block">Day-of Schedule</span>
                    <h1 class="font-serif text-3xl font-bold text-charcoal">Wedding Day Timeline</h1>
                </div>
            </div>

            <div class="bg-white rounded-3xl p-6 sm:p-8 border border-gold/20 shadow-card space-y-6" id="timeline-container">
            </div>
        </section>

        <!-- VIEW 8: MESSAGES BOARD -->
        <section id="view-messages" class="page-view hidden space-y-8">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 bg-white p-6 rounded-3xl border border-gold/30 shadow-card">
                <div>
                    <span class="font-accent text-2xl text-gold block">Vendor Communication</span>
                    <h1 class="font-serif text-3xl font-bold text-charcoal">Messages Board</h1>
                </div>
            </div>

            <div class="bg-white rounded-3xl p-6 sm:p-8 border border-gold/20 shadow-card space-y-4" id="messages-container">
                <div class="p-4 border border-gold/20 rounded-2xl bg-cream">
                    <div class="flex justify-between items-center mb-2">
                        <span class="font-semibold text-charcoal">Grand Napa Estate (Venue)</span>
                        <span class="text-xs text-charcoal-muted">Yesterday</span>
                    </div>
                    <p class="text-sm text-charcoal-light">We have updated your floor plan with the extra 2 banquet tables requested. Looking forward to our walk-through!</p>
                </div>
                <div class="p-4 border border-gold/20 rounded-2xl bg-cream">
                    <div class="flex justify-between items-center mb-2">
                        <span class="font-semibold text-charcoal">Luxe Floral Artistry</span>
                        <span class="text-xs text-charcoal-muted">2 days ago</span>
                    </div>
                    <p class="text-sm text-charcoal-light">The white gardenia sample bouquets are ready for your review this Friday!</p>
                </div>
            </div>
        </section>

    </main>

    <!-- Modal Containers -->
    <div id="modal-add-budget" class="fixed inset-0 bg-charcoal/50 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-white rounded-3xl max-w-md w-full p-6 space-y-4 shadow-2xl border border-gold/30">
            <h3 class="font-serif text-xl font-bold text-charcoal">Add New Budget Item</h3>
            <div class="space-y-3">
                <input type="text" id="new-item-desc" placeholder="Item Description" class="w-full bg-cream border border-gold/30 rounded-xl px-4 py-2 text-sm focus:outline-none">
                <select id="new-item-category" class="w-full bg-cream border border-gold/30 rounded-xl px-4 py-2 text-sm focus:outline-none">
                    <option value="Venue">Venue</option>
                    <option value="Catering">Catering</option>
                    <option value="Photography">Photography</option>
                    <option value="Attire & Beauty">Attire & Beauty</option>
                    <option value="Decor & Florals">Decor & Florals</option>
                    <option value="Entertainment">Entertainment</option>
                </select>
                <input type="number" id="new-item-est" placeholder="Estimated Cost ($)" class="w-full bg-cream border border-gold/30 rounded-xl px-4 py-2 text-sm focus:outline-none">
                <input type="number" id="new-item-act" placeholder="Actual Cost ($)" class="w-full bg-cream border border-gold/30 rounded-xl px-4 py-2 text-sm focus:outline-none">
            </div>
            <div class="flex justify-end space-x-3 pt-2">
                <button onclick="closeAddBudgetModal()" class="px-4 py-2 text-xs font-semibold text-charcoal-muted hover:text-charcoal">Cancel</button>
                <button onclick="saveBudgetItem()" class="gold-gradient-bg text-white px-5 py-2 rounded-xl text-xs font-semibold">Save Item</button>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer class="bg-white border-t border-gold/20 py-8 mt-12 text-center text-xs text-charcoal-muted">
        <div class="max-w-7xl mx-auto px-4">
            <p>&copy; 2027 WedPlanner. All rights reserved. Crafting magical memories worldwide.</p>
        </div>
    </footer>

    <!-- Application Script -->
    <script>
        let appState = {
            budgetItems: [
                { id: 1, desc: "Estate Venue Rental", category: "Venue", est: 15000, act: 15000, status: "Paid" },
                { id: 2, desc: "Catering & Open Bar", category: "Catering", est: 12000, act: 11500, status: "Deposit Paid" },
                { id: 3, desc: "Wedding Photography & Drone", category: "Photography", est: 4500, act: 4500, status: "Paid" },
                { id: 4, desc: "Floral Arrangements & Arch", category: "Decor & Florals", est: 3500, act: 1450, status: "Pending" }
            ],
            vendors: [
                { name: "Grand Napa Estate", category: "Venue", rating: "4.9", price: "$$$$", img: "https://images.unsplash.com/photo-1519167758481-83f550bb49b3?auto=format&fit=crop&w=400&q=80", booked: true },
                { name: "Luxe Floral Artistry", category: "Decor & Florals", rating: "4.8", price: "$$$", img: "https://images.unsplash.com/photo-1526047932273-341f2a7631f9?auto=format&fit=crop&w=400&q=80", booked: true },
                { name: "Aura Cinematic Films", category: "Photography", rating: "5.0", price: "$$$", img: "https://images.unsplash.com/photo-1537633552985-df8429e8048b?auto=format&fit=crop&w=400&q=80", booked: false }
            ],
            guests: [
                { name: "Eleanor Vance", category: "Family", rsvp: "Confirmed", diet: "Vegetarian" },
                { name: "Marcus Thorne", category: "VIP", rsvp: "Confirmed", diet: "None" },
                { name: "Clara Oswald", category: "Friends", rsvp: "Pending", diet: "Gluten-Free" }
            ],
            checklist: [
                { task: "Book Wedding Venue", category: "12 Months Out", done: true },
                { task: "Select Floral Designer", category: "9 Months Out", done: true },
                { task: "Send Out Invitations", category: "4 Months Out", done: false }
            ],
            timeline: [
                { time: "10:00 AM", title: "Bridal Party Hair & Makeup" },
                { time: "02:30 PM", title: "First Look & Couple Portraits" },
                { time: "05:00 PM", title: "Wedding Ceremony" },
                { time: "06:30 PM", title: "Cocktail Hour & Dinner Reception" }
            ]
        };

        function navigateTo(viewId) {
            document.querySelectorAll('.page-view').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.nav-link').forEach(el => el.classList.remove('active'));

            const targetView = document.getElementById(`view-${viewId}`);
            const targetNav = document.getElementById(`nav-${viewId}`);

            if (targetView) targetView.classList.remove('hidden');
            if (targetNav) targetNav.classList.add('active');

            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function toggleMobileMenu() {
            const menu = document.getElementById('mobile-menu');
            menu.classList.toggle('hidden');
        }

        function renderBudgetTable() {
            const tbody = document.getElementById('budget-table-body');
            const filter = document.getElementById('budget-filter-category').value;
            tbody.innerHTML = '';

            let totalSpent = 0;

            appState.budgetItems.forEach(item => {
                totalSpent += Number(item.act || 0);

                if (filter !== 'ALL' && item.category !== filter) return;

                const row = document.createElement('tr');
                row.innerHTML = `
                    <td class="py-3 px-4 font-medium">${item.desc}</td>
                    <td class="py-3 px-4 text-xs text-charcoal-muted">${item.category}</td>
                    <td class="py-3 px-4">$${item.est.toLocaleString()}</td>
                    <td class="py-3 px-4 font-semibold">$${item.act.toLocaleString()}</td>
                    <td class="py-3 px-4"><span class="px-2 py-1 rounded-full text-[10px] font-semibold bg-gold-50 text-gold-dark border border-gold/30">${item.status}</span></td>
                    <td class="py-3 px-4 text-right">
                        <button onclick="deleteBudgetItem(${item.id})" class="text-xs text-rose-custom hover:underline"><i class="fa-solid fa-trash"></i></button>
                    </td>
                `;
                tbody.appendChild(row);
            });

            document.getElementById('budget-spent-display').innerText = `$${totalSpent.toLocaleString()}`;
            document.getElementById('budget-remaining-display').innerText = `$${(45000 - totalSpent).toLocaleString()}`;
            document.getElementById('budget-percent-display').innerText = `${((totalSpent / 45000) * 100).toFixed(1)}% of budget used`;
        }

        function openAddBudgetModal() {
            document.getElementById('modal-add-budget').classList.remove('hidden');
        }

        function closeAddBudgetModal() {
            document.getElementById('modal-add-budget').classList.add('hidden');
        }

        function saveBudgetItem() {
            const desc = document.getElementById('new-item-desc').value;
            const category = document.getElementById('new-item-category').value;
            const est = Number(document.getElementById('new-item-est').value) || 0;
            const act = Number(document.getElementById('new-item-act').value) || 0;

            if (!desc) return;

            appState.budgetItems.push({
                id: Date.now(),
                desc,
                category,
                est,
                act,
                status: act > 0 ? "Committed" : "Pending"
            });

            closeAddBudgetModal();
            renderBudgetTable();
            showToast("Budget item added successfully!");
        }

        function deleteBudgetItem(id) {
            appState.budgetItems = appState.budgetItems.filter(item => item.id !== id);
            renderBudgetTable();
            showToast("Item removed.");
        }

        function renderVendors() {
            const container = document.getElementById('vendor-grid');
            const homeContainer = document.getElementById('home-featured-vendors');
            container.innerHTML = '';
            if (homeContainer) homeContainer.innerHTML = '';

            appState.vendors.forEach((vendor, idx) => {
                const card = `
                    <div class="bg-white rounded-2xl border border-gold/20 overflow-hidden shadow-card hover:shadow-lg transition">
                        <img src="${vendor.img}" alt="${vendor.name}" class="w-full h-48 object-cover">
                        <div class="p-5 space-y-3">
                            <div class="flex justify-between items-start">
                                <div>
                                    <span class="text-[10px] uppercase tracking-wider text-gold-dark font-semibold">${vendor.category}</span>
                                    <h4 class="font-serif text-lg font-bold text-charcoal">${vendor.name}</h4>
                                </div>
                                <span class="text-xs font-semibold bg-gold-50 px-2 py-1 rounded-md text-gold-dark"><i class="fa-solid fa-star text-amber-400 mr-1"></i>${vendor.rating}</span>
                            </div>
                            <div class="flex justify-between items-center text-xs text-charcoal-muted pt-2 border-t border-gold/10">
                                <span>${vendor.price}</span>
                                <span class="font-semibold ${vendor.booked ? 'text-emerald-600' : 'text-gold-dark'}">${vendor.booked ? '<i class="fa-solid fa-check mr-1"></i>Booked' : 'Available'}</span>
                            </div>
                        </div>
                    </div>
                `;
                container.innerHTML += card;
                if (homeContainer && idx < 3) homeContainer.innerHTML += card;
            });
        }

        function renderGuests() {
            const tbody = document.getElementById('guest-table-body');
            tbody.innerHTML = '';

            appState.guests.forEach((guest, index) => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td class="py-3 px-4 font-medium">${guest.name}</td>
                    <td class="py-3 px-4 text-xs text-charcoal-muted">${guest.category}</td>
                    <td class="py-3 px-4"><span class="px-2 py-1 rounded-full text-[10px] font-semibold bg-emerald-50 text-emerald-700">${guest.rsvp}</span></td>
                    <td class="py-3 px-4 text-xs">${guest.diet}</td>
                    <td class="py-3 px-4 text-right">
                        <button onclick="removeGuest(${index})" class="text-xs text-rose-custom hover:underline"><i class="fa-solid fa-trash"></i></button>
                    </td>
                `;
                tbody.appendChild(row);
            });
        }

        function removeGuest(index) {
            appState.guests.splice(index, 1);
            renderGuests();
            showToast("Guest removed.");
        }

        function renderChecklist() {
            const container = document.getElementById('checklist-container');
            const dashContainer = document.getElementById('dash-milestones-list');
            container.innerHTML = '';
            if (dashContainer) dashContainer.innerHTML = '';

            appState.checklist.forEach((item, idx) => {
                const html = `
                    <div class="flex items-center justify-between p-3.5 border border-gold/20 rounded-xl bg-cream/50">
                        <div class="flex items-center space-x-3">
                            <input type="checkbox" ${item.done ? 'checked' : ''} onchange="toggleChecklist(${idx})" class="w-4 h-4 accent-gold cursor-pointer">
                            <span class="text-sm font-medium ${item.done ? 'line-through text-charcoal-muted' : 'text-charcoal'}">${item.task}</span>
                        </div>
                        <span class="text-xs text-gold-dark font-semibold">${item.category}</span>
                    </div>
                `;
                container.innerHTML += html;
                if (dashContainer && !item.done) dashContainer.innerHTML += html;
            });
        }

        function toggleChecklist(idx) {
            appState.checklist[idx].done = !appState.checklist[idx].done;
            renderChecklist();
        }

        function renderTimeline() {
            const container = document.getElementById('timeline-container');
            container.innerHTML = '';

            appState.timeline.forEach(event => {
                container.innerHTML += `
                    <div class="flex items-start space-x-4 p-4 border-l-2 border-gold bg-cream/30 rounded-r-2xl">
                        <span class="font-serif font-bold text-gold-dark text-sm w-24 shrink-0">${event.time}</span>
                        <div>
                            <h4 class="font-semibold text-sm text-charcoal">${event.title}</h4>
                        </div>
                    </div>
                `;
            });
        }

        function showToast(message) {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            toast.className = "bg-charcoal text-white text-xs px-4 py-3 rounded-xl shadow-lg border border-gold/40 animate-fade-in pointer-events-auto flex items-center space-x-2";
            toast.innerHTML = `<i class="fa-solid fa-circle-check text-gold"></i> <span>${message}</span>`;
            container.appendChild(toast);
            setTimeout(() => toast.remove(), 3000);
        }

        window.addEventListener('DOMContentLoaded', () => {
            renderBudgetTable();
            renderVendors();
            renderGuests();
            renderChecklist();
            renderTimeline();
        });
    </script>
</body>
</html>
"""


import streamlit.components.v1 as components

components.html(HTML_CONTENT, height=1200, scrolling=True)