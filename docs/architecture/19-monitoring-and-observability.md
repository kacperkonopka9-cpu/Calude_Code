# 19. Monitoring and Observability

## 19.1 Monitoring Stack

- **Frontend Monitoring:** CloudWatch RUM (Real User Monitoring)
- **Backend Monitoring:** CloudWatch Logs + Metrics
- **Error Tracking:** CloudWatch Insights
- **Performance Monitoring:** CloudWatch Application Insights

---

## 19.2 Key Metrics

**Frontend Metrics:**
- Core Web Vitals (LCP, FID, CLS)
- JavaScript errors (count, stack traces)
- API response times (P50, P95, P99)
- User interactions (button clicks, page views)

**Backend Metrics:**
- Request rate (requests/minute)
- Error rate (errors/total requests %)
- Response time (P50, P95, P99)
- Database query performance (slow query log)
- AI generation time (per project)
- AI cost (EUR per project, daily total)
- Celery queue depth (pending tasks)
- Worker utilization (active/idle workers)

**Alerts:**
- Error rate >5% for 5 minutes
- API response time P95 >1 second
- AI generation failures >10% in 10 minutes
- Daily AI cost >€100 (budget warning)
- Database connection pool exhausted
- Celery queue depth >50 tasks

---

## 19.3 CloudWatch Dashboard

**Widgets:**

1. **API Health**
   - Request rate (line chart)
   - Error rate % (line chart)
   - P50/P95/P99 latency (line chart)

2. **AI Generation**
   - Projects generated/hour (bar chart)
   - Average generation time (line chart)
   - Failure rate % (line chart)
   - Cost per project (line chart)

3. **Infrastructure**
   - ECS CPU utilization (line chart)
   - ECS memory utilization (line chart)
   - Database connections (line chart)
   - Redis memory usage (line chart)

4. **User Activity**
   - Active users (gauge)
   - Batches created/hour (bar chart)
   - Projects exported/hour (bar chart)

---
