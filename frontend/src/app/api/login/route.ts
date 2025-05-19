import { NextResponse } from "next/server";

const DJANGO_JWT_URL = "http://127.0.0.1:8000/api/token/";
export async function POST(request: Request) {
  const body = request.body;
  return new NextResponse(body, { status: 200 });
}
