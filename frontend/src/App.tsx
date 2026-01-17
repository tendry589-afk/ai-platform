import React, { useState } from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <div className="min-h-screen bg-slate-900">
        <nav className="bg-slate-800 border-b border-slate-700 p-4">
          <div className="container mx-auto flex justify-between items-center">
            <h1 className="text-xl font-bold text-white">🤖 AI Platform</h1>
            <div className="space-x-4">
              <Link to="/" className="text-slate-300 hover:text-white">Accueil</Link>
              <Link to="/chatbot" className="text-slate-300 hover:text-white">Chatbot</Link>
              <Link to="/dashboard" className="text-slate-300 hover:text-white">Dashboard</Link>
            </div>
          </div>
        </nav>
        <main className="container mx-auto px-4 py-8">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/chatbot" element={<ChatbotPage />} />
            <Route path="/dashboard" element={<DashboardPage />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

function HomePage() {
  return (
    <div className="text-center">
      <h1 className="text-5xl font-bold text-white mb-6">
        Bienvenue sur <span className="text-blue-400">AI Platform</span>
      </h1>
      <p className="text-xl text-slate-400 mb-8">
        Votre plateforme IA complète avec Chatbot, Recommandations et Analyses
      </p>
      <div className="grid md:grid-cols-3 gap-6 mt-12">
        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700">
          <div className="text-4xl mb-4">💬</div>
          <h3 className="text-xl font-bold text-white mb-2">Chatbot IA</h3>
          <p className="text-slate-400">Conversations intelligentes</p>
        </div>
        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700">
          <div className="text-4xl mb-4">⭐</div>
          <h3 className="text-xl font-bold text-white mb-2">Recommandations</h3>
          <p className="text-slate-400">Suggestions personnalisées</p>
        </div>
        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700">
          <div className="text-4xl mb-4">📊</div>
          <h3 className="text-xl font-bold text-white mb-2">Analytics</h3>
          <p className="text-slate-400">Statistiques en temps réel</p>
        </div>
      </div>
      <div className="mt-12">
        <Link to="/chatbot" className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-3 px-8 rounded-lg transition inline-block">
          🚀 Essayer le Chatbot
        </Link>
      </div>
    </div>
  );
}

function ChatbotPage() {
  const [messages, setMessages] = useState([
    { role: 'assistant', content: 'Bonjour! Je suis votre assistant IA. Comment puis-je vous aider?' }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = () => {
    if (!input.trim()) return;
    setMessages([...messages, { role: 'user', content: input }]);
    setInput('');
    setLoading(true);
    setTimeout(() => {
      setMessages(prev => [...prev, {
        role: 'assistant',
        content: `J'ai bien reçu: "${input}". Je suis un assistant IA en développement!`
      }]);
      setLoading(false);
    }, 1000);
  };

  return (
    <div className="max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold text-white mb-6">💬 Chatbot IA</h1>
      <div className="bg-slate-800 rounded-xl border border-slate-700 h-96 overflow-y-auto p-4 mb-4">
        {messages.map((msg, i) => (
          <div key={i} className={`mb-4 ${msg.role === 'user' ? 'text-right' : 'text-left'}`}>
            <span className={`inline-block px-4 py-2 rounded-lg ${msg.role === 'user' ? 'bg-blue-500 text-white' : 'bg-slate-700 text-white'}`}>
              {msg.content}
            </span>
          </div>
        ))}
        {loading && <p className="text-slate-400">En train d'écrire...</p>}
      </div>
      <div className="flex gap-4">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
          placeholder="Tapez votre message..."
          className="flex-1 px-4 py-3 bg-slate-700 border border-slate-600 rounded-lg text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button onClick={sendMessage} className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-3 px-6 rounded-lg transition">
          Envoyer
        </button>
      </div>
    </div>
  );
}

function DashboardPage() {
  const stats = [
    { label: 'Conversations', value: '12', icon: '💬' },
    { label: 'Messages', value: '48', icon: '📨' },
    { label: 'Recommandations', value: '156', icon: '⭐' },
    { label: 'Prédictions', value: '23', icon: '🔮' },
  ];

  return (
    <div>
      <h1 className="text-3xl font-bold text-white mb-6">📊 Dashboard</h1>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mb-8">
        {stats.map((stat, i) => (
          <div key={i} className="bg-slate-800 p-6 rounded-xl border border-slate-700 text-center">
            <div className="text-3xl mb-2">{stat.icon}</div>
            <div className="text-3xl font-bold text-white">{stat.value}</div>
            <div className="text-slate-400">{stat.label}</div>
          </div>
        ))}
      </div>
      <div className="bg-slate-800 p-6 rounded-xl border border-slate-700">
        <h2 className="text-xl font-bold text-white mb-4">Activité Récente</h2>
        <p className="text-slate-400">Aucune activité pour le moment...</p>
      </div>
    </div>
  );
}

export default App;