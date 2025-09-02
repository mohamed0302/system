import React from 'react';
import { 
  LayoutDashboard, 
  Users, 
  FileText, 
  Calendar, 
  UsersRound,
  X
} from 'lucide-react';
import { ViewType } from '../App';

interface SidebarProps {
  currentView: ViewType;
  onViewChange: (view: ViewType) => void;
  isOpen: boolean;
  onToggle: () => void;
}

const menuItems = [
  { id: 'dashboard' as ViewType, label: 'لوحة التحكم', icon: LayoutDashboard },
  { id: 'students' as ViewType, label: 'الطلاب', icon: Users },
  { id: 'groups' as ViewType, label: 'المجموعات', icon: UsersRound },
  { id: 'exams' as ViewType, label: 'الامتحانات', icon: FileText },
  { id: 'attendance' as ViewType, label: 'الحضور والغياب', icon: Calendar },
];

export const Sidebar: React.FC<SidebarProps> = ({ 
  currentView, 
  onViewChange, 
  isOpen, 
  onToggle 
}) => {
  return (
    <>
      {/* Mobile overlay */}
      {isOpen && (
        <div 
          className="fixed inset-0 bg-black bg-opacity-50 z-40 lg:hidden"
          onClick={onToggle}
        />
      )}
      
      {/* Sidebar */}
      <aside className={`
        fixed lg:static inset-y-0 right-0 z-50
        w-64 bg-white border-l border-gray-200 shadow-lg lg:shadow-none
        transform transition-transform duration-300 ease-in-out
        ${isOpen ? 'translate-x-0' : 'translate-x-full lg:translate-x-0'}
      `}>
        <div className="flex items-center justify-between p-6 border-b border-gray-200 lg:hidden">
          <h2 className="text-lg font-semibold text-gray-900">القائمة</h2>
          <button
            onClick={onToggle}
            className="p-2 rounded-lg hover:bg-gray-100 transition-colors duration-200"
          >
            <X className="w-5 h-5 text-gray-600" />
          </button>
        </div>
        
        <nav className="p-4 space-y-2">
          {menuItems.map((item) => {
            const Icon = item.icon;
            const isActive = currentView === item.id;
            
            return (
              <button
                key={item.id}
                onClick={() => {
                  onViewChange(item.id);
                  onToggle();
                }}
                className={`
                  sidebar-item w-full text-right
                  ${isActive ? 'active' : ''}
                `}
              >
                <Icon className="w-5 h-5 ml-3" />
                <span>{item.label}</span>
              </button>
            );
          })}
        </nav>
        
        <div className="absolute bottom-4 right-4 left-4">
          <div className="bg-gradient-to-r from-primary-500 to-primary-600 rounded-lg p-4 text-white">
            <h3 className="font-semibold mb-1">نظام إدارة الطلاب</h3>
            <p className="text-sm text-primary-100">إصدار 2.0</p>
          </div>
        </div>
      </aside>
    </>
  );
};