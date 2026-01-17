// frontend/src/pages/AnalyticsPage.tsx
import React, { useEffect, useState } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import * as analyticsService from '../services/analytics.service';

export default function AnalyticsPage() {
  const [dashboard, setDashboard] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await analyticsService.getDashboard();
        setDashboard(data);
      } catch (error) {
        console.error('Error fetching analytics:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const chartData = [
    { name: 'Conversations', value: dashboard?.conversations || 0 },
    { name: 'Messages', value: dashboard?.messages || 0 },
    { name: 'Recommendations', value: dashboard?.recommendations || 0 },
    { name: 'Predictions', value: dashboard?.predictions || 0 },
  ];

  return (
    <div className="space-y-6">
      <div className="bg-gradient-to-r from-green-500 to-green-600 text-white p-6 rounded-lg shadow">
        <h1 className="text-2xl font-bold">📊 Analytics Dashboard</h1>
        <p className="text-green-100">Track your AI platform usage</p>
      </div>

      {loading ? (
        <div className="text-center py-12">Loading...</div>
      ) : (
        <>
          {/* Summary Cards */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
            <div className="bg-white rounded-lg shadow p-6">
              <p className="text-slate-600 text-sm">Total Interactions</p>
              <p className="text-3xl font-bold text-slate-900">
                {dashboard?.total_interactions || 0}
              </p>
            </div>
            <div className="bg-white rounded-lg shadow p-6">
              <p className="text-slate-600 text-sm">This Month</p>
              <p className="text-3xl font-bold text-blue-600">+{Math.round((dashboard?.total_interactions || 0) * 0.1)}</p>
            </div>
            <div className="bg-white rounded-lg shadow p-6">
              <p className="text-slate-600 text-sm">Active Days</p>
              <p className="text-3xl font-bold text-purple-600">12</p>
            </div>
            <div className="bg-white rounded-lg shadow p-6">
              <p className="text-slate-600 text-sm">Avg. Session</p>
              <p className="text-3xl font-bold text-orange-600">15m</p>
            </div>
          </div>

          {/* Chart */}
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-xl font-bold text-slate-900 mb-4">Usage Overview</h2>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={chartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="value" fill="#3B82F6" radius={[4, 4, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </>
      )}
    </div>
  );
}
