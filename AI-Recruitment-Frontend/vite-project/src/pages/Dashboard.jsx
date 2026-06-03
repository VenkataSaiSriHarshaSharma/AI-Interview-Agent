import StatCard from "../components/StatCard";

export default function Dashboard() {

  return (

    <div className="p-10">

      <h1 className="text-5xl font-bold text-white">
        Recruitment Dashboard
      </h1>

      <p className="text-slate-400 mt-3">
        AI-Powered Recruitment Intelligence Platform
      </p>

      <div className="grid grid-cols-4 gap-6 mt-10">

        <StatCard
          title="Candidates Screened"
          value="128"
        />

        <StatCard
          title="Interviews Conducted"
          value="94"
        />

        <StatCard
          title="Selected"
          value="38"
        />

        <StatCard
          title="Success Rate"
          value="87%"
        />

      </div>

      <div className="mt-10 bg-slate-900 border border-slate-800 rounded-2xl p-8">

        <h2 className="text-2xl font-bold text-white">
          Welcome
        </h2>

        <p className="text-slate-400 mt-4">
          Manage resume screening, interview assessments,
          candidate evaluations and hiring recommendations
          from a single platform.
        </p>

      </div>

    </div>

  );
}