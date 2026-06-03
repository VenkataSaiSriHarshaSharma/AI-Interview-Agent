import Navbar from "../components/Navbar";
import HeroSection from "../components/HeroSection";
import AnalyticsChart from "../components/AnalyticsChart";
import RecentCandidates from "../components/RecentCandidates";
import StatCard from "../components/StatCard";

export default function Dashboard() {
  return (

    <div className="p-8">

      <Navbar />

      <HeroSection />

      <div className="grid grid-cols-4 gap-6 mt-8">

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

      <div className="mt-8">
        <AnalyticsChart />
      </div>

      <div className="mt-8">
        <RecentCandidates />
      </div>

    </div>
  );
}