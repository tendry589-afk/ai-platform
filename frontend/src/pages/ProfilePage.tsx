// frontend/src/pages/ProfilePage.tsx
import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { RootState } from '../store';
import { logout } from '../store/authSlice';
import { updateProfile } from '../services/auth.service';

export default function ProfilePage() {
  const dispatch = useDispatch();
  const { user } = useSelector((state: RootState) => state.auth);
  const [editing, setEditing] = useState(false);
  const [formData, setFormData] = useState({
    first_name: user?.first_name || '',
    last_name: user?.last_name || '',
  });

  const handleSave = async () => {
    try {
      await updateProfile(formData);
      setEditing(false);
    } catch (error) {
      console.error('Error updating profile:', error);
    }
  };

  const handleLogout = () => {
    dispatch(logout());
    window.location.href = '/login';
  };

  return (
    <div className="space-y-6">
      <div className="bg-gradient-to-r from-orange-500 to-orange-600 text-white p-6 rounded-lg shadow">
        <h1 className="text-2xl font-bold">👤 My Profile</h1>
        <p className="text-orange-100">Manage your account settings</p>
      </div>

      <div className="bg-white rounded-lg shadow p-6">
        <div className="flex items-center space-x-6 mb-6">
          <div className="w-24 h-24 bg-blue-500 rounded-full flex items-center justify-center text-3xl font-bold text-white">
            {user?.first_name?.[0] || user?.username?.[0]?.toUpperCase() || 'U'}
          </div>
          <div>
            <h2 className="text-xl font-bold text-slate-900">
              {user?.first_name} {user?.last_name}
            </h2>
            <p className="text-slate-600">@{user?.username}</p>
            <p className="text-slate-500 text-sm">{user?.email}</p>
          </div>
        </div>

        {editing ? (
          <div className="space-y-4">
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-2">
                  First Name
                </label>
                <input
                  type="text"
                  value={formData.first_name}
                  onChange={(e) => setFormData({ ...formData, first_name: e.target.value })}
                  className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-2">
                  Last Name
                </label>
                <input
                  type="text"
                  value={formData.last_name}
                  onChange={(e) => setFormData({ ...formData, last_name: e.target.value })}
                  className="w-full px-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
            </div>
            <div className="flex space-x-4">
              <button
                onClick={handleSave}
                className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded-lg"
              >
                Save Changes
              </button>
              <button
                onClick={() => setEditing(false)}
                className="bg-slate-300 hover:bg-slate-400 text-slate-900 font-bold py-2 px-6 rounded-lg"
              >
                Cancel
              </button>
            </div>
          </div>
        ) : (
          <div className="flex space-x-4">
            <button
              onClick={() => setEditing(true)}
              className="bg-blue-600 hover:bg-blue-700 text-white font-bold py-2 px-6 rounded-lg"
            >
              Edit Profile
            </button>
            <button
              onClick={handleLogout}
              className="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-6 rounded-lg"
            >
              Logout
            </button>
          </div>
        )}
      </div>

      {/* Account Info */}
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-bold text-slate-900 mb-4">Account Information</h3>
        <div className="space-y-2">
          <p className="text-slate-600">
            <span className="font-medium">Status:</span>{' '}
            <span className="text-green-600">Active</span>
          </p>
          <p className="text-slate-600">
            <span className="font-medium">Verified:</span>{' '}
            <span className={user?.is_verified ? 'text-green-600' : 'text-yellow-600'}>
              {user?.is_verified ? 'Yes' : 'Pending'}
            </span>
          </p>
          <p className="text-slate-600">
            <span className="font-medium">Member since:</span>{' '}
            {new Date(user?.created_at).toLocaleDateString()}
          </p>
        </div>
      </div>
    </div>
  );
}
