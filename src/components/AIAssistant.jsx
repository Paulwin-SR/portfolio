import React, { useState, useRef, useEffect } from 'react';
import { FiSend, FiX, FiMessageSquare } from 'react-icons/fi';
import './AIAssistant.css';

const AIAssistant = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    { text: "Hi there! I'm Paulwin's AI assistant. Ask me anything about his skills, experience, or projects!", isBot: true }
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping]);

  const generateResponse = (query) => {
    const lowerQuery = query.toLowerCase();
    
    // Simple mocked knowledge base matching
    if (lowerQuery.includes('skill') || lowerQuery.includes('tech') || lowerQuery.includes('stack')) {
      return "Paulwin is highly skilled in React, Node.js, Express, MongoDB, and SQL. He also knows Python and Java!";
    } else if (lowerQuery.includes('experience') || lowerQuery.includes('work')) {
      return "He has over 2 years of experience as a Full Stack Developer, currently working at Trivand Technologies.";
    } else if (lowerQuery.includes('project') || lowerQuery.includes('built')) {
      return "Some of his featured projects include an Invoice Management System, a Cyber-bullying Detection AI, and a Food Donation platform. Check out the Projects section for details!";
    } else if (lowerQuery.includes('contact') || lowerQuery.includes('hire') || lowerQuery.includes('email')) {
      return "You can reach him at paulwinpaul2001@gmail.com or call +91 6238541771. He's always open to new opportunities!";
    } else if (lowerQuery.includes('hello') || lowerQuery.includes('hi ')) {
      return "Hello! How can I help you learn more about Paulwin today?";
    } else if (lowerQuery.includes('education') || lowerQuery.includes('study') || lowerQuery.includes('degree')) {
      return "Paulwin holds a B.Tech in Computer Science and Engineering from Lourdes Matha College of Science and Technology.";
    } else {
      return "That's a great question! I'm still learning, but you can find most details scrolling through his portfolio, or contact him directly via the contact form!";
    }
  };

  const handleSend = (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = input.trim();
    setMessages(prev => [...prev, { text: userMessage, isBot: false }]);
    setInput('');
    setIsTyping(true);

    // Simulate network delay for AI "thinking"
    setTimeout(() => {
      const response = generateResponse(userMessage);
      setMessages(prev => [...prev, { text: response, isBot: true }]);
      setIsTyping(false);
    }, 1500);
  };

  return (
    <div className="ai-assistant-container">
      {/* The Floating Character */}
      <div 
        className={`character-mascot ${isOpen ? 'active' : ''}`} 
        onClick={() => setIsOpen(!isOpen)}
      >
        <img src="/chatbot_avatar.png" alt="Paulwin's AI" className="custom-avatar-img" />
        <div className="chat-bubble-indicator">
          <FiMessageSquare />
        </div>
      </div>

      {/* The Chat Window */}
      <div className={`ai-chat-window glass ${isOpen ? 'open' : ''}`}>
        <div className="chat-header">
          <div className="header-info">
            <img src="/chatbot_avatar.png" alt="Mini Avatar" className="mini-avatar-img" />
            <div>
              <h4>Paulwin's AI</h4>
              <span className="status">Online</span>
            </div>
          </div>
          <button className="close-btn" onClick={() => setIsOpen(false)}>
            <FiX size={20} />
          </button>
        </div>
        
        <div className="chat-messages">
          {messages.map((msg, index) => (
            <div key={index} className={`message-bubble ${msg.isBot ? 'bot' : 'user'}`}>
              {msg.text}
            </div>
          ))}
          
          {isTyping && (
            <div className="message-bubble bot typing-indicator">
              <span></span><span></span><span></span>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>
        
        <form className="chat-input-area" onSubmit={handleSend}>
          <input 
            type="text" 
            placeholder="Ask me anything..." 
            value={input}
            onChange={(e) => setInput(e.target.value)}
          />
          <button type="submit" disabled={!input.trim()}>
            <FiSend size={18} />
          </button>
        </form>
      </div>
    </div>
  );
};

export default AIAssistant;
