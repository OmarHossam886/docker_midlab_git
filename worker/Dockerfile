# Build stage
FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /docker_midlab/worker
COPY . .

RUN dotnet publish worker/worker.csproj -c Release -o /app

# Runtime stage
FROM mcr.microsoft.com/dotnet/runtime:7.0
WORKDIR /app
COPY --from=build /app .

ENTRYPOINT ["dotnet", "worker.dll"]
