📊 Interactive Analytics Dashboard + RAG Agent

A modern, responsive, and AI-enhanced analytics dashboard built with Streamlit, featuring authentication, advanced UI styling, Power BI integration, and a Retrieval-Augmented Generation (RAG) agent for intelligent data exploration.

🚀 Features
🎨 Modern UI/UX Enhancements

Glassmorphism cards and blur effects

Animated borders & hover transitions

Pulse effects for live stats

Gradient backgrounds with theme adaptation

Hidden sidebar for clean layout

🔐 Secure Authentication Workflow

Custom login page

Session-based access control

Auto-redirect for unauthorized users

📊 Analytics Dashboard

Embedded Power BI Dashboard inside Streamlit

Clean iframe with branding removed

Auto-resizing responsive layout

Drill-down and filter-based data exploration

📈 Quick Stats Overview

Countries covered

Total data points

Real-time updates

Uptime percentage

🤖 RAG Agent (Retrieval-Augmented Generation)

(Developed based on earlier chats)
Your system also includes a powerful RAG agent that can:

Answer user questions using your dataset

Retrieve context-aware information

Perform semantic search

Support analytics explanation and insights

Help users understand or explore dashboard metrics conversationally

Enhance decision-making through AI-powered guidance

🧩 Modular Architecture

Custom enhanced navigation component

Centralized theme controller

Auth middleware

Reusable CSS styling blocks

📦 Installation
pip install streamlit numpy


Additionally install components used in previous modules:

pip install langchain chromadb sentence-transformers

▶️ Run the Application
streamlit run Dashboard.py
