import React from 'react';
import { Plus, Download, Upload, Settings } from 'lucide-react';

export const QuickActions: React.FC = () => {
  return (
    <div className="card">
      <h2 className="text-xl font-bold text-gray-900 mb-6">إجراءات سريعة</h2>
      
      <div className="space-y-3">
        <button className="w-full btn-primary flex items-center justify-center gap-3 group">
          <Plus className="w-5 h-5 group-hover:rotate-90 transition-transform duration-200" />
          إضافة طالب جديد
        </button>
        
        <button className="w-full btn-secondary flex items-center justify-center gap-3">
          <FileText className="w-5 h-5" />
          إنشاء امتحان جديد
        </button>
        
        <button className="w-full btn-secondary flex items-center justify-center gap-3">
          <Calendar className="w-5 h-5" />
          تسجيل الحضور
        </button>
        
        <div className="border-t border-gray-200 pt-4 mt-6">
          <h3 className="text-sm font-semibold text-gray-700 mb-3">أدوات البيانات</h3>
          <div className="space-y-2">
            <button className="w-full flex items-center gap-3 px-3 py-2 text-sm text-gray-600 hover:bg-gray-50 rounded-lg transition-colors duration-200">
              <Download className="w-4 h-4" />
              تصدير البيانات
            </button>
            <button className="w-full flex items-center gap-3 px-3 py-2 text-sm text-gray-600 hover:bg-gray-50 rounded-lg transition-colors duration-200">
              <Upload className="w-4 h-4" />
              استيراد البيانات
            </button>
            <button className="w-full flex items-center gap-3 px-3 py-2 text-sm text-gray-600 hover:bg-gray-50 rounded-lg transition-colors duration-200">
              <Settings className="w-4 h-4" />
              الإعدادات
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};