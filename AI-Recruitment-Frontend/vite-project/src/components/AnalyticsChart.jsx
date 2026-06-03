import {
  ResponsiveContainer,
  AreaChart,
  Area,
  XAxis,
  YAxis,
  Tooltip
} from "recharts";

const data = [
  { month: "Jan", candidates: 30 },
  { month: "Feb", candidates: 45 },
  { month: "Mar", candidates: 55 },
  { month: "Apr", candidates: 75 },
  { month: "May", candidates: 92 },
  { month: "Jun", candidates: 128 }
];

export default function AnalyticsChart() {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">

      <h2 className="text-xl font-bold text-white mb-6">
        Recruitment Analytics
      </h2>

      <ResponsiveContainer width="100%" height={300}>
        <AreaChart data={data}>
          <XAxis dataKey="month" />
          <YAxis />
          <Tooltip />
          <Area
            type="monotone"
            dataKey="candidates"
            stroke="#22d3ee"
            fill="#0891b2"
          />
        </AreaChart>
      </ResponsiveContainer>

    </div>
  );
}