// frontend/src/services/analytics.service.ts
import api from './api';

export const getDashboard = async () => {
  const response = await api.get('/analytics/dashboard');
  return response.data;
};

export const getUserActivity = async (params?: any) => {
  const response = await api.get('/analytics/activity', { params });
  return response.data;
};

export const exportData = async (format: string) => {
  const response = await api.get(`/analytics/export/${format}`);
  return response.data;
};
