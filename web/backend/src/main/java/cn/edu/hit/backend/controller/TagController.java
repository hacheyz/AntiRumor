package cn.edu.hit.backend.controller;

import cn.edu.hit.backend.pojo.PageBean;
import cn.edu.hit.backend.pojo.Result;
import cn.edu.hit.backend.pojo.Tag;
import cn.edu.hit.backend.service.TagService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/tag")
public class TagController {
  @Autowired
  private TagService tagService;

  @GetMapping("/add")
  public Result add(String name) {
    if(tagService.findByTagName(name) != null){
      return Result.error("标签已存在");
    }
    tagService.addTag(name);
    return Result.success();
  }

  @PostMapping("/pagelist")
  public Result<PageBean<Tag>> pagelist(@RequestBody Map<String, Object> map) {
    return Result.success(tagService.pagelist(map));
  }

  @PostMapping("list")
  public Result<List<Tag>> list() {
    return Result.success(tagService.list());
  }
}