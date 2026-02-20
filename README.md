🧴 Ray’s Cosmetics — System Requirements
✅ 1. Functional Requirements (Startup context)
(What the system DOES)
These come directly from business operations.
🛍️ A. Product Catalog (Core Domain)
Your business sells product variants, not just products.
System must allow:
•	View product categories (Skincare, Makeup, Haircare, etc.)
•	Browse product variants
•	View variant details:
o	Shade
o	Size
o	Price
o	Stock availability
o	Images
•	Search products
•	Filter by:
o	Category
o	Brand
o	Price range
o	Skin type
•	Featured products display
•	Product recommendations
________________________________________
👤 B. User Accounts
•	User registration
•	Login / Logout
•	Profile management
•	Address management
•	Order history
________________________________________
🛒 C. Shopping Cart
•	Add variant to cart
•	Update quantity
•	Remove item
•	Save cart for logged users
•	Calculate totals automatically
________________________________________
💳 D. Orders & Checkout
•	Create order from cart
•	Select delivery address
•	Choose shipping method
•	Calculate delivery cost
•	Generate order number
•	Track order status
Order statuses:
•	Pending
•	Paid
•	Processing
•	Shipped
•	Delivered
•	Cancelled
________________________________________
💰 E. Payments
•	Online payment processing
•	Payment verification
•	Payment status tracking
•	Failed payment handling
________________________________________
📦 F. Inventory Management
•	Track stock per variant
•	Prevent overselling
•	Reduce stock after purchase
•	Restock management
________________________________________
⭐ G. Reviews & Ratings
•	Customers rate products
•	Write reviews
•	Display average ratings
________________________________________
🧑‍💼 H. Admin Management
Admin must:
•	Create categories
•	Add products
•	Add variants
•	Upload images
•	Manage stock
•	View orders
•	Update order status
________________________________________
📢 I. Marketing Features
•	Featured products
•	Discounts
•	Promo codes
•	New arrivals section
________________________________________

⚙️ Non-Functional Requirements 
The non-functional requirements define the operational quality attributes required to ensure Ray’s Cosmetics delivers reliable and scalable online shopping services while operating within startup resource constraints.
________________________________________
🚀 1. Performance Requirements
As a startup e-commerce platform, system responsiveness directly affects customer conversion rates and user satisfaction.
Target Metrics
•	Page response time: ≤ 3 seconds
•	API response time: ≤ 500 ms for catalog queries
•	Product search results: ≤ 1 second
•	Checkout processing: ≤ 2 seconds
Justification
Research shows users abandon websites that load beyond 3 seconds. Early-stage startups must prioritize perceived speed rather than expensive high-performance infrastructure.
Startup Strategy
•	Django ORM optimization
•	Database indexing on:
o	product_variant
o	category
o	price
•	Image compression & CDN later phase
________________________________________
👥 2. Scalability (Load Capacity)
The system must support gradual business growth without immediate migration to microservices.
Initial Capacity Targets
•	Concurrent users: 50–100 users
•	Daily visitors: 500–1,500 users
•	Orders per day: 20–50 orders
Growth Target (Year 2)
•	Concurrent users: 500+
•	Orders/day: 200+
Startup Strategy
•	Modular Monolith architecture
•	Stateless API design
•	Containerization readiness (Docker)
•	Horizontal scaling possible later
This avoids premature microservices complexity.
________________________________________
💾 3. Data Volume Requirements
Data growth expectations are based on typical early e-commerce adoption.
Estimated Year-1 Data Size
•	Products: 300–1,000
•	Product variants: 1,500–5,000
•	Images: 10–50 GB storage
•	Orders stored annually: 5,000–10,000
Startup Strategy
•	PostgreSQL relational database
•	Cloud object storage for images
•	Archive old orders after 24 months
________________________________________
🔄 4. Concurrency Requirements
Multiple customers may attempt to purchase the same cosmetic variant simultaneously.
Operational Targets
•	Support 100 simultaneous cart updates
•	Prevent overselling of stock
•	Transaction success rate ≥ 99%
Technical Controls
•	Database transactions
•	Row-level locking during checkout
•	Atomic stock deduction
•	Idempotent payment confirmation
________________________________________
🔐 5. Security Requirements
Security must protect customer trust without excessive enterprise overhead.
Minimum Security Controls
•	Password hashing using bcrypt
•	HTTPS enforced on all endpoints
•	JWT/session authentication
•	Role-based admin access
•	Payment handled via trusted payment gateway
Security Targets
•	Zero plaintext password storage
•	100% encrypted communication
•	Session timeout after 30 minutes inactivity
Startup focus: secure fundamentals first.
________________________________________
📱 6. Usability Requirements
Since startups compete on customer experience, usability becomes a strategic requirement.
Usability Targets
•	Checkout completed in ≤ 5 steps
•	Mobile usability score ≥ 80/100
•	First-time user purchase flow intuitive without tutorial
Design Goals
•	Mobile-first design
•	Clear product variant selection
•	Minimal checkout friction
________________________________________
🧱 7. Reliability Requirements
Customers must trust that orders and payments are never lost.
Reliability Metrics
•	Order creation success ≥ 99.5%
•	Payment confirmation consistency: 100%
•	Automatic retry for failed background operations
Startup Strategy
•	Database backups every 24 hours
•	Transaction rollback protection
•	Centralized error logging
________________________________________
🛠️ 8. Maintainability Requirements
Startups evolve quickly; therefore, system maintainability is critical.
Architectural Constraints
•	Domain-Driven Design separation:
o	Domain layer
o	Application layer
o	Infrastructure layer
o	Interface layer
Targets
•	New feature integration ≤ 1–2 weeks
•	Bug fix deployment ≤ 24 hours
•	Independent app modification without system-wide refactoring
This allows rapid iteration while keeping technical debt manageable.
________________________________________
📈 9. Availability (SLA)
High availability is desirable but must remain financially realistic for a startup.
Startup SLA Targets
•	System uptime: 99.5%
o	≈ 3.6 hours downtime/month
•	Planned maintenance during low traffic hours
•	Recovery time objective (RTO): ≤ 1 hour
Startup Strategy
•	Single cloud region initially
•	Automated deployment pipeline
•	Upgrade path to multi-region later
