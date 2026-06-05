import {
  Users,
  FileText,
  MessageSquare,
  BarChart3,
} from "lucide-react";

import {
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

const analyticsData = [
  {
    month: "Jan",
    resumes: 12,
    interviews: 8,
  },
  {
    month: "Feb",
    resumes: 18,
    interviews: 14,
  },
  {
    month: "Mar",
    resumes: 25,
    interviews: 20,
  },
  {
    month: "Apr",
    resumes: 32,
    interviews: 28,
  },
  {
    month: "May",
    resumes: 38,
    interviews: 34,
  },
];

export default function Dashboard() {

const resumeReport =
  localStorage.getItem(
    "resumeReport"
  );

const evaluationReport =
  localStorage.getItem(
    "evaluationReport"
  );

const role =
  localStorage.getItem(
    "candidateRole"
  );

const questions =
  JSON.parse(
    localStorage.getItem(
      "interviewQuestions"
    ) || "[]"
  );

const interviewDate =
  localStorage.getItem(
    "lastInterviewDate"
  );

const candidates =
  role ? 1 : 0;

const resumes =
  resumeReport ? 1 : 0;

const interviews =
  questions.length > 0 ? 1 : 0;

const reports =
  evaluationReport ? 1 : 0;

  return (

    <div className="p-8 text-white">

      {/* Header */}

      <div className="mb-10">

        <h1 className="text-5xl font-bold">
          Recruiter Dashboard
        </h1>

        <p className="text-slate-400 mt-3">
          AI Recruitment Analytics &
          Candidate Management
        </p>

      </div>

      {/* Stats Cards */}

      <div className="grid grid-cols-4 gap-6 mb-10">

        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">

          <Users size={35} />

          <h3 className="mt-4 text-slate-400">
            Total Candidates
          </h3>

          <p className="text-4xl font-bold mt-2">
            {candidates}
          </p>

        </div>

        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">

          <FileText size={35} />

          <h3 className="mt-4 text-slate-400">
            Resumes Analyzed
          </h3>

          <p className="text-4xl font-bold mt-2">
            {resumes}
          </p>

        </div>

        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">

          <MessageSquare size={35} />

          <h3 className="mt-4 text-slate-400">
            Interviews Conducted
          </h3>

          <p className="text-4xl font-bold mt-2">
            {interviews}
          </p>

        </div>

        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">

          <BarChart3 size={35} />

          <h3 className="mt-4 text-slate-400">
            Reports Generated
          </h3>

          <p className="text-4xl font-bold mt-2">
            {reports}
          </p>

        </div>

      </div>

      {/* Charts */}

      <div className="grid grid-cols-2 gap-8 mb-10">

        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">

          <h2 className="text-2xl font-bold mb-6">
            Resume Analysis Trend
          </h2>

          <ResponsiveContainer
            width="100%"
            height={300}
          >

            <LineChart data={analyticsData}>

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis dataKey="month" />

              <YAxis />

              <Tooltip />

              <Line
                type="monotone"
                dataKey="resumes"
                stroke="#06b6d4"
                strokeWidth={3}
              />

            </LineChart>

          </ResponsiveContainer>

        </div>

        <div className="bg-slate-900 rounded-3xl p-6 border border-slate-800">

          <h2 className="text-2xl font-bold mb-6">
            Interview Trend
          </h2>

          <ResponsiveContainer
            width="100%"
            height={300}
          >

            <LineChart data={analyticsData}>

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis dataKey="month" />

              <YAxis />

              <Tooltip />

              <Line
                type="monotone"
                dataKey="interviews"
                stroke="#22c55e"
                strokeWidth={3}
              />

            </LineChart>

          </ResponsiveContainer>

        </div>

      </div>

      {/* Activity Feed */}

      <div className="bg-slate-900 rounded-3xl p-8 border border-slate-800">

        <h2 className="text-2xl font-bold mb-6">
          Recent Activity
        </h2>

       <div className="space-y-4">

  <div className="bg-slate-950 p-4 rounded-xl">
    Role Selected:
    {" "}
    {role || "No Role Selected"}
  </div>

  <div className="bg-slate-950 p-4 rounded-xl">
    Questions Generated:
    {" "}
    {questions.length}
  </div>

  <div className="bg-slate-950 p-4 rounded-xl">
    Evaluation:
    {" "}
    {evaluationReport
      ? "Completed"
      : "Pending"}
    </div>

  <div className="bg-slate-950 p-4 rounded-xl">
    Last Interview:
    {" "}
    {interviewDate ||
      "No Interview Yet"}
  </div>

</div>

      </div>

    </div>

  );
}