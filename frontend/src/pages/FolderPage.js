import React, { useState } from 'react';
import SummaryComponent from '../components/SummaryComponent';

const FolderPage = () => {
    const [items, setItems] = useState([
        { id: 1, name: "Item 1" },
        { id: 2, name: "Item 2" },
        { id: 3, name: "Item 3" },
        { id: 4, name: "Item 4" }
    ]);

    return (
        <div className='inline-flex'>
            {items.map(item => (
                <SummaryComponent key={item.id} />
            ))}
        </div>
    );
};

export default FolderPage;
