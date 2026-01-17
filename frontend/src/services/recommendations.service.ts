// frontend/src/services/recommendations.service.ts
import api from './api';

export const getRecommendations = async (limit = 10) => {
  const response = await api.get('/recommendations/', { params: { limit } });
  return response.data;
};

export const getRecommendationById = async (id: string) => {
  const response = await api.get(`/recommendations/${id}`);
  return response.data;
};

export const provideFeedback = async (id: string, feedback: any) => {
  const response = await api.post(`/recommendations/${id}/feedback`, feedback);
  return response.data;
};
