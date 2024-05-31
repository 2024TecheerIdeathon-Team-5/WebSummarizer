import React, { useState } from 'react';

const SummaryComponent = () => {
    const [imageUrl, setImageUrl] = useState('');
    const [summary, setSummary] = useState('요약글입니다.');
    const [externalUrl, setExternalUrl] = useState('');

    // 해당 페이지로 가는 함수
    const handlebutton = () => {
        window.location.href = externalUrl;
    }

    return (
        <div className='flex flex-col justify-between w-[289px] h-[356px] rounded-[27px] bg-white border-2 border-primary m-4 p-2'>
            <div className='self-start w-full p-0'>
                <img src={imageUrl} alt="Loaded Image" className="w-full h-auto" />
            </div> 
            <div className='self-center w-full p-2'>{summary}</div>
            <div className='self-end pr-3'>
                <button onClick={handlebutton}>
                    more-{'>'}
                </button>
            </div>
        </div>
    );
};

export default SummaryComponent;