import {
  LayoutDashboard,
  FileText,
  MessageSquare,
  BarChart3
} from "lucide-react";

export default function Sidebar() {

  return (

    <div className="h-screen w-72 bg-slate-950 border-r border-slate-800 p-6">

      <h1 className="text-3xl font-bold text-cyan-400 mb-10">
        AI Recruiter
      </h1>

      <div className="space-y-8">

        <div className="flex items-center gap-3 text-slate-300 hover:text-cyan-400 cursor-pointer transition">
          <LayoutDashboard />
          <span>Dashboard</span>
        </div>

        <div className="flex items-center gap-3 text-slate-300 hover:text-cyan-400 cursor-pointer transition">
          <FileText />
          <span>Resume Screening</span>
        </div>

        <div className="flex items-center gap-3 text-slate-300 hover:text-cyan-400 cursor-pointer transition">
          <MessageSquare />
          <span>Interview</span>
        </div>

        <div className="flex items-center gap-3 text-slate-300 hover:text-cyan-400 cursor-pointer transition">
          <BarChart3 />
          <span>Reports</span>
        </div>

      </div>

    </div>

  );
}