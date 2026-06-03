import { motion } from "framer-motion";

export default function HeroSection() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 40 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
      className="relative overflow-hidden rounded-3xl bg-gradient-to-r from-cyan-500 via-blue-600 to-indigo-700 p-10 text-white shadow-2xl"
    >
      <div className="absolute right-0 top-0 h-72 w-72 rounded-full bg-white/10 blur-3xl"></div>

      <h1 className="text-5xl font-bold">
        AI Recruitment Intelligence
      </h1>

      <p className="mt-4 text-lg text-cyan-100 max-w-3xl">
        Hire smarter with AI-powered resume screening,
        interview assessment and candidate evaluation.
      </p>

      <div className="mt-8 flex gap-4">
        <button className="rounded-xl bg-white px-6 py-3 font-semibold text-slate-900 hover:scale-105 transition">
          Start Screening
        </button>

        <button className="rounded-xl border border-white px-6 py-3 font-semibold hover:bg-white hover:text-slate-900 transition">
          View Reports
        </button>
      </div>
    </motion.div>
  );
}