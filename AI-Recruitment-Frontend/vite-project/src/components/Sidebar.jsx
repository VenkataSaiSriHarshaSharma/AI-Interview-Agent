import {
  LayoutDashboard,
  FileText,
  MessageSquare,
  BarChart3,
  Settings,
} from "lucide-react";

import { Link, useLocation } from "react-router-dom";

export default function Sidebar() {
  const location = useLocation();

  const menuItems = [
    {
      name: "Dashboard",
      icon: <LayoutDashboard size={20} />,
      path: "/",
    },
    {
      name: "Resume Screening",
      icon: <FileText size={20} />,
      path: "/resume",
    },
    {
      name: "Interview",
      icon: <MessageSquare size={20} />,
      path: "/interview",
    },
    {
      name: "Reports",
      icon: <BarChart3 size={20} />,
      path: "/reports",
    },
    {
      name: "Settings",
      icon: <Settings size={20} />,
      path: "/settings",
    },
  ];

  return (
    <div className="h-screen w-72 bg-slate-950 border-r border-slate-800 flex flex-col">

      {/* Logo Section */}
      <div className="p-6 border-b border-slate-800">

        <h1 className="text-3xl font-bold text-cyan-400">
          AI Recruiter
        </h1>

        <p className="text-slate-400 text-sm mt-2">
          Recruitment Intelligence Platform
        </p>

      </div>

      {/* Navigation */}
      <div className="flex-1 p-4">

        <div className="space-y-3">

          {menuItems.map((item) => (

            <Link
              key={item.name}
              to={item.path}
              className={`flex items-center gap-4 p-4 rounded-xl transition-all duration-300 ${
                location.pathname === item.path
                  ? "bg-cyan-500 text-white shadow-lg"
                  : "text-slate-300 hover:bg-slate-800 hover:text-cyan-400"
              }`}
            >
              {item.icon}

              <span className="font-medium">
                {item.name}
              </span>

            </Link>

          ))}

        </div>

      </div>

      {/* Footer */}
      <div className="p-6 border-t border-slate-800">

        <div className="bg-slate-900 rounded-xl p-4">

          <p className="text-slate-400 text-sm">
            Platform Version
          </p>

          <p className="text-cyan-400 font-bold mt-1">
            v4.0
          </p>

        </div>

      </div>

    </div>
  );
}