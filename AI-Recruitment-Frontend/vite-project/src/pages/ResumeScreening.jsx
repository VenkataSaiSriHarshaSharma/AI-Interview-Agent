import { useState } from "react";
import api from "../services/api";

export default function ResumeScreening() {

  const [file, setFile] = useState(null);

  const [role, setRole] = useState("");

  const [report, setReport] = useState("");

  const uploadResume = async () => {

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
  };

  return (

    <div className="p-8">

      <h1 className="text-4xl text-white font-bold mb-6">
        Resume Screening
      </h1>

      <input
        className="border p-3 mb-4 block"
        placeholder="Target Role"
        onChange={(e)=>
          setRole(
            e.target.value
          )
        }
      />

      <input
        type="file"
        onChange={(e)=>
          setFile(
            e.target.files[0]
          )
        }
      />

      <button
        className="bg-cyan-500 text-white px-6 py-3 rounded-xl mt-4"
        onClick={uploadResume}
      >
        Analyze Resume
      </button>

      {report && (

        <div className="mt-8 bg-slate-900 p-6 rounded-xl text-white">

          <pre
            style={{
              whiteSpace: "pre-wrap"
            }}
          >
            {report}
          </pre>

        </div>

      )}

    </div>

  );
}