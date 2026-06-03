import { useState } from "react";
import { Upload, FileText, Brain, CheckCircle } from "lucide-react";
import api from "../services/api";

export default function ResumeScreening() {

  const [file, setFile] = useState(null);
  const [role, setRole] = useState("");
  const [report, setReport] = useState("");
  const [loading, setLoading] = useState(false);

  const uploadResume = async () => {

    if (!file || !role) {
      alert("Please select a resume and enter a role");
      return;
    }

    try {

      setLoading(true);

      const formData = new FormData();

      formData.append(
        "resume",
        file
      );

      formData.append(
        "role",
        role
      );

      const response = await api.post(
        "/screen-resume",
        formData
      );

      setReport(
        response.data.report
      );

    } catch (error) {

      console.log(error);

      alert("Resume analysis failed");

    } finally {

      setLoading(false);

    }

  };

  return (

    <div className="p-8 text-white">

      {/* HEADER */}

      <div className="mb-10">

        <h1 className="text-5xl font-bold">
          Resume Screening
        </h1>

        <p className="text-slate-400 mt-3">
          AI-powered candidate evaluation and skill matching
        </p>

      </div>

      {/* TOP GRID */}

      <div className="grid grid-cols-12 gap-6">

        {/* LEFT PANEL */}

        <div className="col-span-7">

          <div className="bg-slate-900 border border-slate-800 rounded-3xl p-8">

            <h2 className="text-2xl font-semibold mb-6">
              Upload Candidate Resume
            </h2>

            <input
              type="text"
              placeholder="Target Role (e.g. AI Engineer)"
              value={role}
              onChange={(e) =>
                setRole(e.target.value)
              }
              className="
                w-full
                bg-slate-950
                border
                border-slate-700
                rounded-xl
                px-4
                py-4
                mb-6
                text-white
                outline-none
                focus:border-cyan-400
              "
            />

            <label
              className="
                flex
                flex-col
                items-center
                justify-center
                border-2
                border-dashed
                border-slate-700
                rounded-2xl
                h-64
                cursor-pointer
                hover:border-cyan-400
                transition
              "
            >

              <Upload
                size={50}
                className="text-cyan-400"
              />

              <p className="mt-4 text-slate-300">
                Drag & Drop Resume
              </p>

              <p className="text-sm text-slate-500">
                PDF / DOCX Supported
              </p>

              <input
                type="file"
                hidden
                onChange={(e) =>
                  setFile(
                    e.target.files[0]
                  )
                }
              />

            </label>

            {file && (

              <div className="mt-4 text-cyan-400">

                Selected File:
                {" "}
                {file.name}

              </div>

            )}

            <button
              onClick={uploadResume}
              disabled={loading}
              className="
                mt-6
                w-full
                bg-cyan-500
                hover:bg-cyan-600
                py-4
                rounded-xl
                font-semibold
                transition
              "
            >
              {loading
                ? "Analyzing Resume..."
                : "Analyze Resume"}
            </button>

          </div>

        </div>

        {/* RIGHT PANEL */}

        <div className="col-span-5">

          <div className="grid gap-5">

            <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

              <div className="flex items-center gap-3">

                <Brain className="text-cyan-400" />

                <h3 className="font-semibold">
                  AI Analysis
                </h3>

              </div>

              <p className="text-slate-400 mt-4">
                Resume skills and experience
                will be analyzed here.
              </p>

            </div>

            <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

              <div className="flex items-center gap-3">

                <FileText className="text-cyan-400" />

                <h3 className="font-semibold">
                  Resume Match
                </h3>

              </div>

              <h2 className="text-4xl font-bold text-cyan-400 mt-4">
                --
              </h2>

            </div>

            <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

              <div className="flex items-center gap-3">

                <CheckCircle className="text-green-400" />

                <h3 className="font-semibold">
                  Recommendation
                </h3>

              </div>

              <p className="text-slate-400 mt-4">
                Awaiting analysis...
              </p>

            </div>

          </div>

        </div>

      </div>

      {/* REPORT SECTION */}

      {report && (

        <div className="mt-10">

          <div className="bg-slate-900 border border-slate-800 rounded-3xl p-8">

            <h2 className="text-3xl font-bold mb-6">
              AI Resume Report
            </h2>

            <div className="bg-slate-950 rounded-2xl p-6">

              <pre
                className="whitespace-pre-wrap text-slate-300"
              >
                {report}
              </pre>

            </div>

          </div>

        </div>

      )}

    </div>

  );
}