import React from 'react';
import { Menu, RefreshCw, GraduationCap } from 'lucide-react';
import { ViewType } from '../App';

interface HeaderProps {
  onMenuClick: () => void;
  currentView: ViewType;
}

const viewTitles: Record<ViewType, string> = {
  dashboard: 'لوحة التحكم',
  students: 'إدارة الطلاب',
  exams: 'إدارة الامتحانات',
  attendance: 'متابعة الحضور',
  groups: 'إدارة المجموعات'
};

export const Header: React.FC<HeaderProps> = ({ onMenuClick, currentView }) => {
  return (
    <header className="bg-white border-b border-gray-200 px-6 py-4 flex items-center justify-between shadow-sm">
      <div className="flex items-center gap-4">
        <button
          onClick={onMenuClick}
          className="lg:hidden p-2 rounded-lg hover:bg-gray-100 transition-colors duration-200"
        >
          <Menu className="w-5 h-5 text-gray-600" />
        </button>
        
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 bg-primary-600 rounded-lg flex items-center justify-center">
            <GraduationCap className="w-5 h-5 text-white" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-gray-900">
              {viewTitles[currentView]}
            </h1>
            <p className="text-sm text-gray-500">نظام إدارة الطلاب</p>
          </div>
        </div>
      </div>

      <div className="flex items-center gap-4">
        <button className="p-2 rounded-lg hover:bg-gray-100 transition-colors duration-200 group">
          <RefreshCw className="w-5 h-5 text-gray-600 group-hover:rotate-180 transition-transform duration-300" />
        </button>
        
        <div className="w-8 h-8 bg-gradient-to-br from-primary-500 to-primary-600 rounded-full flex items-center justify-center">
          <span className="text-white text-sm font-medium">أ</span>
        </div>
      </div>
    </header>
  );
};