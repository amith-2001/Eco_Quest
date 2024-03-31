import '/flutter_flow/flutter_flow_util.dart';
import 'mainpage_widget.dart' show MainpageWidget;
import 'package:flutter/material.dart';

class MainpageModel extends FlutterFlowModel<MainpageWidget> {
  ///  State fields for stateful widgets in this page.

  final unfocusNode = FocusNode();

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    unfocusNode.dispose();
  }
}
