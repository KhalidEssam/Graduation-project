import React , { ChangeEvent, useState } from 'react';
import { useRef } from 'react';
import { ReactFlow } from 'reactflow';
import './App.css';
import Acc from './components/Acc';
import Gyro from './components/Gyro';
import Video from './components/Video';
import Report from './components/report';
import Processing from './components/processing';
import Frquency from './components/Frquency';
import Repcount from './components/Repcount';
import useClickTracker from "./hooks/clicktracker";
import useArrowConnect from './hooks/connectgraph';





interface CSVUploadButtonProps {
  onFileUpload: (file: File) => void;
}

const CSVUploadButton: React.FC<CSVUploadButtonProps> = ({ onFileUpload }) => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleFileChange = (event: ChangeEvent<HTMLInputElement>) => {
    const fileList = event.target.files;
    if (fileList && fileList.length > 0) {
      setSelectedFile(fileList[0]);
    }
  };

  const handleUpload = () => {
    if (selectedFile) {
      onFileUpload(selectedFile);
      setSelectedFile(null);
    }
  };

  return (
    <div>
      <input
        type="file"
        // multiple
        accept=".csv,video/mp4"
        onChange={handleFileChange}
      />
      <button className="button" onClick={handleUpload} disabled={!selectedFile}>
        Upload
      </button>
    </div>
  );
};


const LaunchAppButton: React.FC = () => {
  const handleLaunchApp = () => {
    window.open('http://localhost:8000');
  };

  return (
    <button onClick={handleLaunchApp} className="button">
      Launch Another App
    </button>
  );
};


function App() {
  
  const handleFileUpload = (file: File) => {
    // Handle the file upload here
    console.log(file);
  };

  
const clickedElements =useClickTracker();




const handleLaunchApp = () => {
  window.open('http://localhost:8000');
};

const handleClick = () => {
  const modalitiess: string[] = [];
  const reports: string[] = [];
  const method: { [key: string]: any } = {};
  const hasAcc = clickedElements.some(element => element.id.includes('Acc'));
  const hasModel = clickedElements.some(element => element.id.includes('CNN_LSTM'));
  const hasreport= clickedElements.some(element => element.id.includes('classification'));
  const hasfreq= clickedElements.some(element => element.id.includes('Frquency'));
  const hascount= clickedElements.some(element => element.id.includes('Repcount'));
  let Model=''

  if(hasAcc)
  {
    modalitiess.push("acc");
  }
  if(hascount)
  {
    reports.push("rep_count");
  }
  if(hasfreq)
  {
    reports.push("freq");
  }
  if(hasreport)
  {
    reports.push("classification");
  }
  
  const hasGry = clickedElements.some(element => element.id.includes('Gyro'));
  
  if(hasGry)
  {
    modalitiess.push("gyro");
  }

  const video = clickedElements.some(element => element.id.includes('Video'));
  if(video)
  {
    modalitiess.push("pose");
  }

  if(hasModel && video)
  {
    Model= "cnn-lstm";
    method['pose'] = "cnn-lstm"
  }
  if(hasModel && hasAcc || hasModel && hasGry)
  {
    Model= "cnn-lstm";
    method['sensor'] = "cnn-lstm"
  }
  if(hasAcc && video||hasGry && video)
  {
    method['ensemble'] = true
  }
  else{
    method['ensemble'] = false
  }
 
  const jsonData = JSON.stringify({"modalities": modalitiess,
  "processing": method,
  "report": reports});
  const blob = new Blob([jsonData], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'data.json';
  link.click();
  URL.revokeObjectURL(url);
 handleLaunchApp();
};

  return (
    
    <main>
      <form method="POST">
      <div className="container">
      <div  className="rightcontainer">
      <div  className="reportcontainer">
      
      <p>Clicked Elements:</p>
      <ul>
        {
          
        clickedElements.map((element, index) => (
          <li key={index}>
            {element.tagName}
            {element.id && `#${element.id}`}
            {element.classList && element.classList.join('.')}
          </li>
        ))}
      </ul>

      </div> 
      <div  className="inputcontainer">
      
      <p>Input Elements:</p>
      
      </div> 

      <div  className="processingcontainer">
      
      <p>Processing Elements:</p>
      

      </div> 

      <div  className="outputcontainer">
      
      <p>Output Elements:</p>
      

      </div> 

      </div>
      <div  className="leftcontainer"> 
      <Acc /> <br></br>
      
      <span id='text'>Gyroscope</span>
      <Gyro /><br></br><br></br><br></br>
      <span id='text'>Video</span>
      <Video /><br></br><br></br><br></br>
      <span id='text'>Accelerometer</span>
      <Report/><br></br><br></br><br></br> <br></br>
      <span id='text'>CNN-LSTM Model</span>
      <Processing/><br></br><br></br><br></br><br></br>
      <span id='text'> Classification Report</span>
      <Frquency/><br></br><br></br><br></br><br></br>
      <span id='text'> Frquency Report</span>
      <Repcount/><br></br><br></br><br></br><br></br>
      <span id='text'> Repeatition counting Report</span>
      </div>

      

        
      </div>
      <div className='upploader' ><h1>Upload your Data-set</h1>
      <CSVUploadButton onFileUpload={handleFileUpload} />
      </div>
     
     

      </form>
      <span> 
      <h1>Launch Steam App</h1>
      <button onClick={handleClick} className="button">Generate Code</button>
      
      </span>
      
    </main>
    
  );
}

export default App;
