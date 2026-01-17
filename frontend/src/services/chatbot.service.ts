// frontend/src/services/chatbot.service.ts
import api from './api';

export const createConversation = async (data: any) => {
  const response = await api.post('/chatbot/conversations', data);
  return response.data;
};

export const getConversations = async (skip = 0, limit = 10) => {
  const response = await api.get('/chatbot/conversations', {
    params: { skip, limit },
  });
  return response.data;
};

export const getConversation = async (conversationId: string) => {
  const response = await api.get(`/chatbot/conversations/${conversationId}`);
  return response.data;
};

export const sendMessage = async (data: any) => {
  const response = await api.post('/chatbot/chat', data);
  return response.data;
};

export const getMessages = async (conversationId: string, skip = 0, limit = 50) => {
  const response = await api.get(`/chatbot/conversations/${conversationId}/messages`, {
    params: { skip, limit },
  });
  return response.data;
};

export const deleteConversation = async (conversationId: string) => {
  const response = await api.delete(`/chatbot/conversations/${conversationId}`);
  return response.data;
};
