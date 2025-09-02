import React from 'react';
import { Users, FileText, Calendar, TrendingUp, Award, AlertCircle } from 'lucide-react';
import { useData } from '../context/DataContext';
import { StatsCard } from './StatsCard';
import { RecentActivity } from './RecentActivity';
import { QuickActions } from './QuickActions';

export const Dashboard: React.FC = () => {
  const { students, exams, absences, examGrades, loading } = useData();

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    );
  }

  // Calculate statistics
  const totalStudents = students.length;
  const totalExams = exams.length;
  const totalAbsences = absences.length;
  const averageGrade = examGrades.length > 0 
    ? examGrades.reduce((sum, grade) => sum + grade.الدرجة, 0) / examGrades.length 
    : 0;

  const recentAbsences = absences.slice(-5);
  const recentGrades = examGrades.slice(-5);

  return (
    <div className="space-y-8 animate-fade-in">
      {/* Welcome Section */}
      <div className="bg-gradient-to-r from-primary-600 to-primary-700 rounded-2xl p-8 text-white">
        <h1 className="text-3xl font-bold mb-2">مرحباً بك في نظام إدارة الطلاب</h1>
        <p className="text-primary-100 text-lg">
          تابع أداء طلابك وإدارة الامتحانات والحضور بسهولة
        </p>
      </div>

      {/* Statistics Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <StatsCard
          title="إجمالي الطلاب"
          value={totalStudents.toString()}
          icon={Users}
          color="primary"
          trend="+5%"
        />
        <StatsCard
          title="الامتحانات"
          value={totalExams.toString()}
          icon={FileText}
          color="success"
          trend="+2"
        />
        <StatsCard
          title="حالات الغياب"
          value={totalAbsences.toString()}
          icon={AlertCircle}
          color="warning"
          trend="-10%"
        />
        <StatsCard
          title="متوسط الدرجات"
          value={averageGrade.toFixed(1)}
          icon={Award}
          color="success"
          trend="+3.2"
        />
      </div>

      {/* Main Content Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Recent Activity */}
        <div className="lg:col-span-2">
          <RecentActivity 
            recentAbsences={recentAbsences}
            recentGrades={recentGrades}
          />
        </div>

        {/* Quick Actions */}
        <div>
          <QuickActions />
        </div>
      </div>
    </div>
  );
};