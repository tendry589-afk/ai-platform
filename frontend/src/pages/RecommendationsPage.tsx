// frontend/src/pages/RecommendationsPage.tsx
import React, { useEffect, useState } from 'react';
import * as recommendationsService from '../services/recommendations.service';

interface Recommendation {
  id: string;
  item_id: string;
  item_type: string;
  item_title: string;
  score: number;
  confidence: number;
  reason: string;
  algorithm: string;
}

export default function RecommendationsPage() {
  const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRecommendations = async () => {
      try {
        const data = await recommendationsService.getRecommendations();
        setRecommendations(data);
      } catch (error) {
        console.error('Error fetching recommendations:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchRecommendations();
  }, []);

  return (
    <div className="space-y-6">
      <div className="bg-gradient-to-r from-purple-500 to-purple-600 text-white p-6 rounded-lg shadow">
        <h1 className="text-2xl font-bold">⭐ Personalized Recommendations</h1>
        <p className="text-purple-100">AI-powered suggestions just for you</p>
      </div>

      {loading ? (
        <div className="text-center py-12">Loading...</div>
      ) : recommendations.length === 0 ? (
        <div className="text-center py-12 bg-white rounded-lg shadow">
          <div className="text-6xl mb-4">📋</div>
          <p className="text-slate-600">No recommendations yet</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {recommendations.map((rec) => (
            <div
              key={rec.id}
              className="bg-white rounded-lg shadow p-6 hover:shadow-lg transition"
            >
              <div className="flex items-start justify-between">
                <div>
                  <span className="inline-block px-2 py-1 text-xs font-semibold bg-purple-100 text-purple-600 rounded mb-2">
                    {rec.item_type}
                  </span>
                  <h3 className="text-lg font-semibold text-slate-900">
                    {rec.item_title || rec.item_id}
                  </h3>
                  <p className="text-slate-600 text-sm mt-2">{rec.reason}</p>
                </div>
                <div className="text-right">
                  <div className="text-2xl font-bold text-purple-600">
                    {Math.round(rec.score * 100)}%
                  </div>
                  <div className="text-xs text-slate-500">match</div>
                </div>
              </div>

              <div className="mt-4 pt-4 border-t border-slate-200">
                <div className="flex items-center justify-between text-sm text-slate-500">
                  <span>Confidence: {Math.round(rec.confidence * 100)}%</span>
                  <span className="capitalize">{rec.algorithm.replace('_', ' ')}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
