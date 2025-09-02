import React from 'react';
import { LucideIcon } from 'lucide-react';

interface StatsCardProps {
  title: string;
  value: string;
  icon: LucideIcon;
  color: 'primary' | 'success' | 'warning' | 'error';
  trend?: string;
}

const colorClasses = {
  primary: {
    bg: 'bg-primary-50',
    icon: 'text-primary-600',
    trend: 'text-primary-600'
  },
  success: {
    bg: 'bg-success-50',
    icon: 'text-success-600',
    trend: 'text-success-600'
  },
  warning: {
    bg: 'bg-warning-50',
    icon: 'text-warning-600',
    trend: 'text-warning-600'
  },
  error: {
    bg: 'bg-error-50',
    icon: 'text-error-600',
    trend: 'text-error-600'
  }
};

export const StatsCard: React.FC<StatsCardProps> = ({ 
  title, 
  value, 
  icon: Icon, 
  color, 
  trend 
}) => {
  const colors = colorClasses[color];

  return (
    <div className="card hover:scale-105 transition-transform duration-200">
      <div className="flex items-center justify-between">
        <div>
          <p className="text-sm font-medium text-gray-600 mb-1">{title}</p>
          <p className="text-3xl font-bold text-gray-900">{value}</p>
          {trend && (
            <p className={`text-sm font-medium ${colors.trend} mt-1`}>
              {trend}
            </p>
          )}
        </div>
        <div className={`w-12 h-12 ${colors.bg} rounded-lg flex items-center justify-center`}>
          <Icon className={`w-6 h-6 ${colors.icon}`} />
        </div>
      </div>
    </div>
  );
};