# app/clients/profile_client.py
# gRPC client stub usage example.
# Assumes you have generated profile_pb2 and profile_pb2_grpc from .proto files.

import grpc                     # grpc client
from typing import Optional

# from proto import profile_pb2, profile_pb2_grpc  # Uncomment when you have generated stubs.

class ProfileClient:
    def __init__(self, target: str):
        """
        target: "host:port" for gRPC server
        """
        self.target = target
        self.channel = None
        self.stub = None

    def connect(self):
        if self.channel is None:
            self.channel = grpc.insecure_channel(self.target)
            # self.stub = profile_pb2_grpc.ProfileServiceStub(self.channel)

    def fetch_profile(self, user_id: str, auth_token: Optional[str] = None) -> dict:
        """
        Sequential gRPC call. No retry/backoff and no graceful degradation implemented
        (matches original design).
        """
        self.connect()
        # Example gRPC call (pseudocode):
        # metadata = []
        # if auth_token:
        #     metadata = [("authorization", f"Bearer {auth_token}")]
        # req = profile_pb2.GetProfileRequest(user_id=user_id)
        # resp = self.stub.GetProfile(req, metadata=metadata, timeout=2.0)
        # return {"bio": resp.bio, "avatar_url": resp.avatar_url}
        #
        # Since the proto isn't provided here, return a placeholder dict to show structure:
        # NOTE: proto generates a pb2 file to serialize between Python -> Profobuf and vice versa, not included here.
        return {"bio": "This is a stubbed bio", "avatar_url": "https://example.com/avatar.png"}
