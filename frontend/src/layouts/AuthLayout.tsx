// frontend/src/layouts/AuthLayout.tsx
import React from 'react';
import { Outlet } from 'react-router-dom';

export default function AuthLayout() {
  return (
    <div className="min-h-screen bg-slate-100">
      <Outlet />
    </div>
  );
}
