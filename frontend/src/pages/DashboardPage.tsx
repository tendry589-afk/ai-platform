// frontend/src/pages/DashboardPage.tsx
import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import { RootState } from '../store';
import * as analyticsService from '../services/analytics.service';

export default function DashboardPage() {
  const { user } = useSelector((state: RootState) => state.auth);
  const [stats, setStats] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const data = await analyticsService.getDashboard();
        setStats(data);
      } catch (error) {
        console.error('Error fetching stats:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchStats();
  }, []);

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold text-slate-900">
          Welcome, {user?.first_name || user?.username}! 👋
        </h1>
        <p className="text-slate-600 mt-2">
          Here's your AI Platform dashboard
        </p>
      </div>

      {loading ? (
        <div className="text-center py-12">Loading...</div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {/* Stats Cards */}
          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-slate-600 text-sm">Conversations</p>
                <p className="text-3xl font-bold text-slate-900">
                  {stats?.conversations || 0}
                </p>
              </div>
              <div className="text-4xl">💬</div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-slate-600 text-sm">Messages</p>
                <p className="text-3xl font-bold text-slate-900">
                  {stats?.messages || 0}
                </p>
              </div>
              <div className="text-4xl">📨</div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-slate-600 text-sm">Recommendations</p>
                <p className="text-3xl font-bold text-slate-900">
                  {stats?.recommendations || 0}
                </p>
              </div>
              <div className="text-4xl">⭐</div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-slate-600 text-sm">Predictions</p>
                <p className="text-3xl font-bold text-slate-900">
                  {stats?.predictions || 0}
                </p>
              </div>
              <div className="text-4xl">🔮</div>
            </div>
          </div>
        </div>
      )}

      {/* Quick Links */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <a
          href="/chatbot"
          className="bg-gradient-to-br from-blue-500 to-blue-600 rounded-lg shadow p-6 text-white hover:shadow-lg transition"
        >
          <h3 className="text-xl font-bold mb-2">💬 Chatbot</h3>
          <p>Start a conversation with AI</p>
        </a>

        <a
          href="/recommendations"
          className="bg-gradient-to-br from-purple-500 to-purple-600 rounded-lg shadow p-6 text-white hover:shadow-lg transition"
        >
          <h3 className="text-xl font-bold mb-2">⭐ Recommendations</h3>
          <p>Get personalized suggestions</p>
        </a>

        <a
          href="/analytics"
          className="bg-gradient-to-br from-green-500 to-green-600 rounded-lg shadow p-6 text-white hover:shadow-lg transition"
        >
          <h3 className="text-xl font-bold mb-2">📊 Analytics</h3>
          <p>View your usage statistics</p>
        </a>

        <a
          href="/profile"
          className="bg-gradient-to-br from-orange-500 to-orange-600 rounded-lg shadow p-6 text-white hover:shadow-lg transition"
        >
          <h3 className="text-xl font-bold mb-2">👤 Profile</h3>
          <p>Manage your account</p>
        </a>
      </div>
    </div>
  );
}
