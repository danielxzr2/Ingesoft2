const request = require('supertest');
const app = require('../src/app');
describe('API Endpoints', () => {
    test('GET / should return welcome message', async () => {
        const response = await request(app).get('/');
        expect(response.status).toBe(200);
        expect(response.body.message).toBe('Hola, DevOps!');
    });
    test('GET /health should return OK status', async () => {
        const response = await request(app).get('/health');
        expect(response.status).toBe(200);
        expect(response.body.status).toBe('OK');
    });
    test('GET /version should return version 1.0.0', async () => {
        const response = await request(app).get('/version');
        expect(response.status).toBe(200);
        expect(response.body).toEqual({ version: '1.0.0' });
    });
});
